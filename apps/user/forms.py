from django import forms
from django.db import models
from django.contrib.auth.forms import User
from .models import nota


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={"class": "input-field", "placeholder": "Usuario"}))
    password = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={
        "class": "input-field", "placeholder": "Contraseña"
    }))


class registerUser(forms.Form):

    username = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={"class": "input-field", "placeholder": "Usuario"}))
    email = forms.EmailField(max_length=60, widget=forms.EmailInput(attrs={
        "class": "input-field", "placeholder": "email@ejemplo.com"
    }))
    password1 = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={
        "class": "input-field", "placeholder": "Contraseña"
    }))
    password2 = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={
        "class": "input-field", "placeholder": "Confirmar contraseña"
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
    descripcion = forms.CharField(max_length=400, widget=forms.Textarea(
        attrs={"placeholder": "Description"}))
    color = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={"value": "#FFFFFF"}))

    class Meta():
        model = nota
        fields = ['fecha', 'titulo', 'descripcion', 'color']
