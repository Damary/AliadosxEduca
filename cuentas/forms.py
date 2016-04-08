# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User


class RegistroUserForm(forms.Form):

    username = forms.CharField(min_length=5)
    email = forms.EmailField()
    password = forms.CharField(min_length=5, widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
   

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

    def clean_password2(self):
        
        """Comprueba que password y password2 sean iguales."""
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        print '¡¡¡¡¡¡¡¡¡¡¡¡', password2, password, '!!!!!!!!!!!'
        if password != password2:
            print 'sadjasd', forms.ValidationError('Las contraseñas no coinciden.')
            raise forms.ValidationError('Las contraseñas no coinciden.')
        else:
            print '0000000000000000000000000000000'

        return password2

class SomeForm(forms.Form):
    name = forms.CharField(error_messages={'required':'Error Missing Field , Please Fill this Field'})