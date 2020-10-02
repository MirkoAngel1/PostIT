from django import forms
from django.db import models
from django.contrib.auth.forms import User
from .models import nota


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={"class": "input-field", "placeholder": "User"}))
    password = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={
        "class": "input-field", "placeholder": "Password"
    }))


class registerUser(forms.Form):

    username = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={"class": "input-field", "placeholder": "User"}))
    email = forms.EmailField(max_length=60, widget=forms.EmailInput(attrs={
        "class": "input-field", "placeholder": "email@example.com"
    }))
    password1 = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={
        "class": "input-field", "placeholder": "Password"
    }))
    password2 = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={
        "class": "input-field", "placeholder": "Confirme Password"
    }))

    class Meta():
        model = User
        filter = ['username', 'email', 'password1',
                  'password2', ]


class registernota(forms.ModelForm):
    fecha = forms.DateField(widget=forms.DateInput(
        attrs={"placeholder": "day/month/year"}))
    titulo = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={"placeholder": "Tittle"}))
    descripcion = forms.CharField(max_length=60, widget=forms.Textarea(
        attrs={"placeholder": "Description"}))
    color = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={"value": "#2000FF"}))

    class Meta():
        model = nota
        fields = ['fecha', 'titulo', 'descripcion', 'color']
