# -*- coding: utf-8 -*-
from django import forms

class LoginForm (forms.Form):

	username = forms.CharField()
	clave = forms.CharField(widget = forms.PasswordInput())
