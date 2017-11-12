from django import forms

from .models import Tweet


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', required=True, max_length=64)
    password = forms.CharField(label='Password', required=True)


class TweetForm(forms.Form):
    message = forms.CharField(max_length=140, required=True)
