from django import forms
from django.db import models
from django.contrib.auth.forms import User


class changeEmailForm(forms.Form):

    email = forms.EmailField(max_length=60, widget=forms.EmailInput(attrs={
        "class": "input-field", "value": "", "placeholder": "Current Email"
    }))
    email2 = forms.EmailField(max_length=60, widget=forms.EmailInput(attrs={
        "class": "input-field", "placeholder": "New Email"
    }))
    email3 = forms.EmailField(max_length=60, widget=forms.EmailInput(attrs={
        "class": "input-field", "placeholder": "Repeat New Email"
    }))

    class Meta():
        model = User
        filter = ["email"]


class changePassForm(forms.Form):
    password = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={
        "class": "input-field"
    }))
    password2 = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={
        "class": "input-field"
    }))
    password3 = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={
        "class": "input-field"
    }))

    class Meta():
        model = User
        filter = ['password']


class changeUsernameForm(forms.Form):
    username = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={"class": "input-field", "placeholder": "Current Username"}))
    username2 = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={"class": "input-field", "placeholder": "New Username"}))
    username3 = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={"class": "input-field", "placeholder": "Repeat New Username"}))

    class Meta():
        model = User
        filter = ['username']
