from django import forms
from django.contrib.auth.models import User
from django.utils.http import base36_to_int
from django.utils.translation import gettext_lazy as _
from ourwedding.models import MessageFromGuest, Guest
from ourwedding.models import Profile
from ourwedding.tokens import login_token_generator


class SecretCodeForm(forms.Form):
    access_code = forms.CharField(required=True, max_length=255)
    next = forms.CharField(required=False, max_length=255)

    def clean_access_code(self):
        access_code = self.cleaned_data.get("access_code", "").lower()
        if len(access_code.split("-")) != 3:
            raise forms.ValidationError(_("Wrong access code format"))

        a, b, user_pk = self.cleaned_data["access_code"].split("-")
        user_pk = base36_to_int(user_pk)
        try:
            user = User.objects.get(pk=user_pk)
        except User.DoesNotExist:
            raise forms.ValidationError(_("Secret Code not Valid"))
        if not login_token_generator.check_token(
            user, self.cleaned_data.get("access_code")
        ):
            raise forms.ValidationError(_("Access Code Expired. Require a New one."))

        return user_pk


class RequestCodeForm(forms.Form):
    email = forms.EmailField(required=True)


class CustomSlider(forms.CheckboxInput):
    input_type = "checkbox"
    template_name = "widgets/slider.html"

    def __init__(self, *args, **kwargs):
        super(CustomSlider, self).__init__(*args, **kwargs)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            "phone",
            "language",
            "comes_from",
            "dietary_restrictions",
            "is_attending",
            "has_car",
            "needs_van",
        )
        widgets = {
            "dietary_restrictions": forms.TextInput(),
            "comes_from": forms.TextInput(),
            "is_attending": CustomSlider(),
            "has_car": CustomSlider(),
            "needs_van": CustomSlider(),
        }


class GuestEditForm(forms.ModelForm):
    """Form used by one guest to edit other guest's information."""

    class Meta:
        model = Profile
        fields = ("is_attending", "is_child")
        widgets = {
            "is_attending": CustomSlider(),
            "is_child": CustomSlider(),
        }

    def clean_first_name(self):
        instance = getattr(self, "instance", None)
        if instance and instance.id:
            return instance.first_name
        else:
            return self.cleaned_data["first_name"]


class GuestCreateForm(forms.ModelForm):
    """Form used by a guest to add a new guest."""

    class Meta:
        model = Guest
        fields = (
            "first_name",
            "last_name",
            "email",
            "phone",
            "dietary_restrictions",
            "is_attending",
            "is_child",
        )

        widgets = {
            "dietary_restrictions": forms.TextInput(),
            "is_child": CustomSlider(),
            "is_attending": CustomSlider(),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = MessageFromGuest
        fields = ("message",)


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ("first_name", "last_name", "email")
        widgets = {
            "email": forms.EmailInput(),
        }
