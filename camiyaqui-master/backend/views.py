import csv
import io
import json

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import Context, Template
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.views.generic.base import View

from backend.forms import GuestForm, UploadFileForm, EmailGuest, GuestEdit
from ourwedding.forms import GuestEditForm
from ourwedding.models import MessageFromGuest, Guest
from backend.models import Message, News
from ourwedding.models import Profile
from ourwedding.tokens import login_token_generator


class BackendLogin(LoginView):
    template_name = "backend/index.html"
    success_url = reverse_lazy("bcknd-guest-list")
    redirect_authenticated_user = True


class GuestList(LoginRequiredMixin, View):
    template_name = "backend/guest_list.html"

    def get(self, request):
        guests_waiting = Guest.objects.exclude(is_child=True).all()
        children = Guest.objects.filter(is_child=True).all()
        guests_approved = User.objects.all()
        coming_guests = Profile.objects.filter(is_attending=True).count()
        coming_guests += (
            Guest.objects.filter(is_attending=True).exclude(is_child=True).count()
        )
        unsure_guests = Profile.objects.filter(is_attending=None).count()
        not_coming_guests = Profile.objects.filter(is_attending=False).count()
        need_van = (
            Profile.objects.filter(needs_van=True).count()
            + Guest.objects.filter(needs_van=True).count()
        )

        return render(
            request,
            self.template_name,
            {
                "guests_waiting": guests_waiting,
                "guests_approved": guests_approved,
                "coming_guests": coming_guests,
                "unsure_guests": unsure_guests,
                "not_coming_guests": not_coming_guests,
                "need_van": need_van,
                "children": children,
            },
        )


class GuestApprove(LoginRequiredMixin, View):
    def post(self, request, **kwargs):
        guest = get_object_or_404(Guest, pk=kwargs["pk"])
        if not guest.email:
            messages.warning(request, "Not possible to approve a guest without e-mail")
            return render(request, "backend/guest_list.html")
        try:
            user = User.objects.get(email=guest.email)
        except User.DoesNotExist:
            user = User.objects.create(
                first_name=guest.first_name,
                last_name=guest.last_name,
                email=guest.email,
                username=guest.email,
            )
        user.save()
        user.profile.dietary_restrictions = guest.dietary_restrictions
        user.profile.is_attending = guest.is_attending
        user.profile.is_child = guest.is_child
        user.profile.phone = guest.phone
        user.profile.has_car = guest.has_car
        if guest.invited_by:
            user.profile.invited_by = guest.invited_by
            if guest.invited_by.profile.group:
                user.profile.group = guest.invited_by.profile.group
        user.profile.comes_from = guest.comes_from
        user.save()
        guest.delete()
        user.profile.send_code()
        return redirect(reverse_lazy("bcknd-guest-list"))


class ProfileDetails(LoginRequiredMixin, DetailView):
    model = Profile
    context_object_name = "guest"
    template_name = "backend/guest_detail.html"


class GuestDetails(LoginRequiredMixin, DetailView):
    model = Guest
    context_object_name = "guest"
    template_name = "backend/guest_detail.html"


class ProfileEdit(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = GuestEdit
    template_name = "backend/guest_edit.html"
    success_url = reverse_lazy("bcknd-guest-list")


class MessageList(LoginRequiredMixin, ListView):
    model = Message
    template_name = "backend/messages_list.html"
    context_object_name = "messages"


class ExportGuests(LoginRequiredMixin, View):
    def get(self, *args):
        response = HttpResponse(content_type="text/json")
        response["Content-Disposition"] = 'attachment; filename="guests.json"'
        data = list(User.objects.values())
        response.write(json.dumps(data, cls=DjangoJSONEncoder))
        return response


class MessageSend(LoginRequiredMixin, View):
    """View to send the message to all the people on the list, filtered by language.
    It will not send the message to the same person twice.
    """

    context_name = "message"
    template_name = "backend/message_dashboard.html"

    def get(self, request, **kwargs):
        message = get_object_or_404(Message, pk=kwargs["pk"])
        form = EmailGuest()
        return render(
            request,
            template_name=self.template_name,
            context={"message": message, "form": form},
        )

    def post(self, request, **kwargs):
        message = Message.objects.get(pk=kwargs["pk"])
        num_sent = message.send_all()
        form = EmailGuest()
        return render(
            request,
            template_name=self.template_name,
            context={"message": message, "form": form},
        )


class MessageSendTest(LoginRequiredMixin, View):
    def post(self, request, **kwargs):
        message = get_object_or_404(Message, pk=kwargs["pk"])
        form = EmailGuest(request.POST)
        if form.is_valid():
            guest = get_object_or_404(User, email=form.cleaned_data["email"])
            message.send(guest, check_language=False)
        return redirect(reverse_lazy("message-detail", args=(message.pk,)))


class MessageDetail(LoginRequiredMixin, DetailView):
    model = Message
    template_name = "backend/message_detail.html"
    context_object_name = "message"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["form"] = EmailGuest()
        return data


class MessagePreview(LoginRequiredMixin, View):
    def get(self, request, **kwargs):
        message = get_object_or_404(Message, pk=kwargs["pk"])
        context = {}
        guest = request.user
        context.update({"guest": guest})
        context.update({"token": login_token_generator.make_token(guest)})
        context = Context(context)
        tmpl_html = Template(message.template_html)
        template = tmpl_html.render(context=context)
        return HttpResponse(template)


class MessagesFromGuestList(LoginRequiredMixin, ListView):
    model = MessageFromGuest
    template_name = "backend/messages_list.html"
    context_object_name = "messages"


class MessageCreate(LoginRequiredMixin, CreateView):
    model = Message
    fields = ["language", "subject", "template_html", "template_txt"]

    def get_success_url(self):
        return reverse("message-list")


class MessageUpdate(LoginRequiredMixin, UpdateView):
    model = Message
    context_object_name = "message"
    fields = ["language", "subject", "template_html", "template_txt"]


class UploadContactsView(LoginRequiredMixin, View):
    def get(self, request):
        form = UploadFileForm()
        return render(request, "backend/upload_file.html", {"form": form})

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = io.TextIOWrapper(request.FILES["file"].file)
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    pass
                if not User.objects.filter(email=row["email"]).exists():
                    new_user = User.objects.create(
                        username=row["email"],
                        email=row["email"],
                        first_name=row["first_name"],
                        last_name=row["last_name"],
                    )
                    new_user.profile.language = row["language"]
                    new_user.save()
                else:
                    print(f'User {row["first_name"]} {row["last_name"]} already in DB')
                line_count += 1

        return render(request, "backend/upload_file.html", {"form": form})


class ListNewsView(LoginRequiredMixin, ListView):
    model = News
    context_object_name = "news"
    template_name = "backend/news_list.html"


class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    fields = ["language", "title", "message"]
    success_url = reverse_lazy("list-news")
    template_name = "backend/news_create.html"
