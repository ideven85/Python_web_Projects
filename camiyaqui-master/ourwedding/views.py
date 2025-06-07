import json
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import NON_FIELD_ERRORS
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.translation import gettext as _
from django.utils.translation import _trans
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, UpdateView, DetailView, CreateView, FormView
from django.views.generic.base import View, TemplateView

from ourwedding.models import MessageFromGuest, Guest
from backend.models import InternalMessage
from ourwedding.forms import (
    SecretCodeForm,
    RequestCodeForm,
    ProfileForm,
    GuestEditForm,
    GuestCreateForm,
    RegisterForm,
)
from ourwedding.mixins import GuestMixin
from ourwedding.models import Profile, Group, Anecdote


class Index(GuestMixin, View):
    def get(self, request):
        return render(request, "ourwedding/index.html")


class Register(View):
    form = RegisterForm
    template_name = "ourwedding/register.html"

    def get(self, request):
        form = self.form()
        if request.session.get("guest"):
            form = self.form(request.GET)
            guest = User.objects.get(pk=request.session.get("guest"))
            error_msg = _(
                "You are already logged in as {}. Are you sure you want to register again?"
            )
            form.errors[NON_FIELD_ERRORS] = [error_msg.format(guest)]
            messages.warning(request, error_msg.format(guest))
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            if form.cleaned_data["email"]:
                if User.objects.filter(email=form.cleaned_data["email"]).exists():
                    messages.info(
                        request,
                        _("The email you used is already registered. Try logging in."),
                    )
                    return redirect(reverse_lazy("guest-login"))
            guest = form.save()
            InternalMessage.objects.create(
                message="New guest registered and requires attention: {}".format(guest)
            )

            return render(request, self.template_name)
        return render(request, self.template_name, {"form": form})


class GuestLogin(View):
    def get(self, request):
        """Handles the login if the user has an access code. If the form includes a next parameter it will
        redirect to that page.
        This is handy for sending e-mails that allow users to go directly to a special page.
        """
        form = SecretCodeForm(request.GET)
        if form.is_valid():
            user = User.objects.get(pk=form.cleaned_data.get("access_code"))
            login(request, user)
            request.user = user
            request.session["guest"] = user.pk
            request.session[_trans] = user.profile.language
            messages.success(request, _(f"Welcome back {user}!"))
            if form.cleaned_data.get("next"):
                return redirect(form.cleaned_data.get("next"))
            return redirect("home")

        return render(request, "ourwedding/login.html", {"secret_form": form})

    def post(self, request):
        """Handles the request of a new access code. It checks if the guest exists and sends an e-mail. If the guest
        doesn't exist, it will send an e-mail to the admins warning about this action.
        """
        form = RequestCodeForm(request.POST)
        if form.is_valid():
            if User.objects.filter(email=form.cleaned_data["email"]).exists():
                guest = User.objects.get(email=form.cleaned_data["email"])
                guest.profile.send_code()
                messages.info(request, _("Activation code sent. Check your e-mail"))
                return render(request, "ourwedding/login.html")
            else:
                if Profile.objects.filter(email=form.cleaned_data["email"]).exists():
                    messages.warning(
                        request,
                        _(
                            "We are reviewing your request to join the party. Be patient."
                        ),
                    )
                else:
                    messages.error(
                        request,
                        _("That e-mail is not on our database. Consider registering"),
                    )
                InternalMessage.objects.create(
                    message="Tried to request code for non-existing email: {}".format(
                        form.cleaned_data["email"]
                    )
                )
        else:
            messages.error(request, _("There were errors processing your form"))
        return render(request, "ourwedding/login.html")


class GuestProfile(GuestMixin, SuccessMessageMixin, UpdateView):
    template_name = "ourwedding/profile.html"
    form_class = ProfileForm
    context_object_name = "guest"
    success_url = reverse_lazy("guest-profile")
    success_message = _("Thanks for updating your profile.")

    def get_object(self, queryset=None):
        user = User.objects.get(pk=self.request.session.get("guest"))
        return user.profile


class Contact(GuestMixin, SuccessMessageMixin, CreateView):
    model = MessageFromGuest
    fields = ("message",)
    template_name = "ourwedding/new_message.html"
    success_message = _(
        "Thank you for the message! We will come back to you as soon as possible"
    )
    success_url = reverse_lazy("contact")

    def form_valid(self, form):
        obj = form.save(commit=False)
        user = User.objects.get(pk=self.request.session.get("guest"))
        obj.guest = user
        obj.save()
        return redirect(self.success_url)


class GroupView(GuestMixin, View):
    template_name = "ourwedding/group_detail.html"

    def get(self, request):
        user = User.objects.get(pk=self.request.session.get("guest"))
        if not user.profile.group:
            group = Group.objects.create(name=user)
            user.profile.group = group
            user.save()

        guest_invites = Guest.objects.filter(invited_by=user)
        return render(
            request,
            self.template_name,
            {"group": user.profile.group, "invites": guest_invites},
        )


class GuestEdit(GuestMixin, UpdateView):
    template_name = "ourwedding/profile_base.html"
    form_class = GuestEditForm
    context_object_name = "guest"
    success_url = reverse_lazy("group")
    model = Profile

    def dispatch(self, request, *args, **kwargs):
        """Making sure that only authors can update stories"""
        obj = self.get_object()
        current_guest = Profile.objects.get(pk=self.request.session.get("guest"))
        if obj.group != current_guest.group:
            messages.warning(
                request, _("You can't edit a guest from a different group")
            )
            return redirect(reverse_lazy("group"))
        return super(GuestEdit, self).dispatch(request, *args, **kwargs)


class GuestAdd(GuestMixin, View):
    def get(self, request):
        form = GuestCreateForm()
        return render(request, "ourwedding/add_guest.html", {"form": form})

    def post(self, request):
        form = GuestCreateForm(request.POST)
        if form.is_valid():
            new_guest = form.save(commit=False)
            curr_guest = User.objects.get(pk=request.session.get("guest"))
            new_guest.invited_by = curr_guest
            new_guest.save()
            curr_guest.save()
            return redirect(reverse_lazy("RSVP"))
        return render(request, "ourwedding/add_guest.html", {"form": form})


class CreateMessage(GuestMixin, CreateView):
    model = Anecdote
    template_name = "ourwedding/new_message.html"
    success_url = reverse_lazy("list-messages")
    fields = ("message",)

    def form_valid(self, form):
        form.instance.guest = Profile.objects.get(pk=self.request.session.get("guest"))
        return super(CreateMessage, self).form_valid(form)


class ViewMessages(GuestMixin, ListView):
    model = Anecdote
    template_name = "ourwedding/messages.html"
    context_object_name = "messages"

    def get_queryset(self):
        guest = Profile.objects.get(pk=self.request.session.get("guest"))
        return Anecdote.objects.filter(guest=guest)


class UpdateGuestAjax(GuestMixin, View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UpdateGuestAjax, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        u, user_pk, option, value = data["id"].split("_")
        if u == "u":
            try:
                user = User.objects.get(pk=user_pk)
            except User.DoesNotExist:
                return JsonResponse(
                    status=500, data={"message": "problem getting the user"}
                )
            guest = user.profile
        elif u == "g":
            try:
                guest = Guest.objects.get(pk=user_pk)
            except Guest.DoesNotExist:
                return JsonResponse(
                    status=500, data={"message": "problem getting the guest"}
                )
        else:
            raise Exception("Badly form request")
        if option == "attending":
            if value == "yes":
                guest.is_attending = True
            elif value == "no":
                guest.is_attending = False
            elif value == "none":
                guest.is_attending = None
            else:
                return JsonResponse(
                    status=500, data={"message": "problem updating guest"}
                )
        elif option == "child":
            guest.is_child = data["new_status"]
        elif option == "van":
            guest.needs_van = data["new_status"]
        elif option == "car":
            guest.has_car = data["new_status"]
        elif option == "prewed":
            guest.pre_wedding = data["new_status"]
        elif option == "postwed":
            guest.post_wedding = data["new_status"]
        else:
            return JsonResponse(status=500, data={"message": "problem updating guest"})

        guest.save()

        return JsonResponse(status=200, data={"message": "updated"})


class EventView(GuestMixin, TemplateView):
    template_name = "ourwedding/event.html"


class WeddingView(GuestMixin, TemplateView):
    template_name = "ourwedding/wedding.html"


class PreWeddingView(GuestMixin, TemplateView):
    template_name = "ourwedding/pre_wedding.html"


class AccommodationView(GuestMixin, TemplateView):
    template_name = "ourwedding/accommodation.html"


class BuenosAiresView(GuestMixin, TemplateView):
    template_name = "ourwedding/buenosaires.html"


class TangoView(GuestMixin, TemplateView):
    template_name = "ourwedding/tango.html"


class SecretCodeValidationView(View):
    def get(self, request, secret_code):
        if not Profile.objects.filter(secret_code=secret_code).exists():
            return redirect(reverse_lazy("guest-login"))

        guest = Profile.objects.get(secret_code=secret_code)
        request.session["guest"] = guest.pk
        request.session[LANGUAGE_SESSION_KEY] = guest.language
        return redirect(reverse_lazy("save-the-date"))


class SaveTheDateView(GuestMixin, TemplateView):
    def get_template_names(self):
        guest_pk = self.request.session.get("guest")
        guest = Profile.objects.get(pk=guest_pk)
        if guest.language == "en":
            return "savethedate/index_en.html"
        return "savethedate/index_es.html"


class HelpView(TemplateView):
    template_name = "ourwedding/help.html"


class GuestList(GuestMixin, ListView):
    model = User
    template_name = "ourwedding/guest_list.html"
    context_object_name = "guests"

    ordering = ["last_name", "-first_name"]


def index_forbidden(request):
    return render(request, "ourwedding/index_forbidden.html")
