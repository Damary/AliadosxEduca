# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User


class UserProfile(forms.Form):

	username = forms.CharField(min_length=5)
	email = forms.EmailField()
	password = forms.CharField(min_length=5, widget=forms.PasswordInput())
	password2 = forms.CharField(widget=forms.PasswordInput())
	nombre = forms.CharField()
	apellido = forms.CharField()

	username = forms.CharField(
	min_length=5,
	widget=forms.TextInput(attrs={'class': 'form-control'}))

	email = forms.EmailField(
		widget=forms.EmailInput(attrs={'class': 'form-control'}))

	password = forms.CharField(
		min_length=5,
		widget=forms.PasswordInput(attrs={'class': 'form-control'}))

	password2 = forms.CharField(
		min_length=5,
		widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	   

	def clean_username(self):
		print 'clean_username'
		"""Comprueba que no exista un username igual en la db"""
		username = self.cleaned_data['username']
		print User.objects.filter(username=username), 'username', username
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