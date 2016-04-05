# -*- coding: utf-8 -*-
from django import forms

class LoginForm (forms.Form):

	Usuario = forms.CharField()
	Clave = forms.CharField(widget = forms.PasswordInput())
