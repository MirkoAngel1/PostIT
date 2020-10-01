from django import forms
from django.db import models
from django.contrib.auth.forms import User


class changeEmailForm(forms.Form):

    email = forms.EmailField(max_length=60, widget=forms.EmailInput(attrs={
        "class": "input-field"
    }))
    email2 = forms.EmailField(max_length=60, widget=forms.EmailInput(attrs={
        "class": "input-field"
    }))
    email3 = forms.EmailField(max_length=60, widget=forms.EmailInput(attrs={
        "class": "input-field"
    }))

    class Meta():
        model = User
        filter = ["email"]


class changeUsernameForm(forms.Form):
    username = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={"class": "input-field"}))
    username2 = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={"class": "input-field"}))
    username3 = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={"class": "input-field"}))

    class Meta():
        model = User
        filter = ['username']
