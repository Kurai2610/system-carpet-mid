from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario


class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['email', 'nombre', 'apellido', 'password']
