# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User

from aliado.models import *

class UserProfile(forms.Form):

	usuario = forms.CharField(min_length=5)
	email = forms.EmailField()
	password = forms.CharField(min_length=5, widget=forms.PasswordInput())
	repetir_password = forms.CharField(min_length=5,widget=forms.PasswordInput())
	nombre = forms.CharField()
	apellido = forms.CharField()

	usuario = forms.CharField(
	min_length=5,
	widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Escriba su Nombre de Usuario'}))

	email = forms.EmailField(
		widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Escriba su Correo Electrónico'}))

	nombre = forms.CharField(
		widget = forms.TextInput(attrs = {'class': 'form-control','placeholder':'Escriba su Nombre'}))

	apellido = forms.CharField(
		widget= forms.TextInput(attrs = {'class': 'form-control', 'placeholder':'Escriba su Apellido'}))
	
	rtn_aliado = forms.CharField(
		widget= forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'RTN de la Empresa' }))
	

	password = forms.CharField(
		min_length=5,
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Escriba su Contraseña' }))

	repetir_password = forms.CharField(
		min_length=5,
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme su Contraseña'}))
	   

	def clean_usuario(self):
		
		usuario = self.cleaned_data['usuario']
		
		if User.objects.filter(username=usuario):
			raise forms.ValidationError('Nombre de usuario ya registrado.')
		return usuario

	def clean_email(self):
		
		email = self.cleaned_data['email']
		if User.objects.filter(email=email):
			raise forms.ValidationError('Ya existe un email igual en la db.')
		return email

	def clean_repetir_password(self):
		
		"""Comprueba que password y repetir_password sean iguales."""
		password = self.cleaned_data['password']
		repetir_password = self.cleaned_data['repetir_password']
		
		if password != repetir_password:
			
			raise forms.ValidationError('Las contraseñas no coinciden.')
		else:
			

			return repetir_password



class SomeForm(forms.Form):
	name = forms.CharField(error_messages={'required':'Error Missing Field , Please Fill this Field'})


class DirectivaFormulario(forms.Form):

	class Meta:
		model = DirectivaAliado
		exclude = ['usuario_creador', 'usuario_modifico', 'aliado', 'contacto_rsc_rse', 'contacto_primario']

class AliadoFormulario(forms.Form):
	
	departamento = forms.ModelChoiceField(label="Departamento ", queryset=Departamento.objects.all())
	tipo_aliado = forms.ModelChoiceField(label = "Tipo de Aliado", queryset = TipoAliado.objects.all().order_by('nombre'))
	
	class Meta:
		model = Aliado
		fields = ['nombre_comercial', 'razon_social','rtn_aliado', 'direccion', 'correo',
		'telefono',  'logo', 'tipo_aliado', 'rubro_aliado', 'departamento', 'municipio', 
		'aldea' ,'rsc_rse', 'rtn_fundacion', 'nombre_fundacion', 'direccion_fundacion']

		exclude = ['usuario_creador', 'usuario_modifico', 'fecha_creacion', 'fecha_modifico']
