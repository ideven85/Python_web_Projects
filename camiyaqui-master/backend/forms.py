from django import forms

from ourwedding.models import Profile


class GuestEdit(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class GuestForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("language", "is_attending", "is_child")


class UploadFileForm(forms.Form):
    file = forms.FileField()


class EmailGuest(forms.Form):
    email = forms.EmailField()
