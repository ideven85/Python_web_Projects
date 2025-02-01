from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "body", "active"]


class SearchForm(forms.Form):
    query = forms.CharField()
