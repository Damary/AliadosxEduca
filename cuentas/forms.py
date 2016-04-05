# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User


class RegistroUserForm(forms.Form):

    username = forms.CharField(min_length=5)
    email = forms.EmailField()
    clave = forms.CharField(min_length=5, widget=forms.PasswordInput())
    clave2 = forms.CharField(widget=forms.PasswordInput())
   

    def clean_username(self):
        print 'clean_username'
        """Comprueba que no exista un username igual en la db"""
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nombre de usuario ya registrado.')
        return username

    def clean_email(self):
        print 'clean_email'
        """Comprueba que no exista un email igual en la db"""
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Ya existe un email igual en la db.')
        return email

    def clean_clave2(self):
        print 'clean_password2'
        """Comprueba que password y password2 sean iguales."""
        clave = self.cleaned_data['clave']
        clave2 = self.cleaned_data['clave2']
        if clave != clave2:
            print 'sadjasd', forms.ValidationError('Las contraseñas no coinciden.')
            raise forms.ValidationError('Las contraseñas no coinciden.')
        else:
            print '0000000000000000000000000000000'

        return clave2