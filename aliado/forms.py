# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from aliado.models import *

class AliadoFormulario(ModelForm):
	
	departamento = forms.ModelChoiceField(label="Departamento ", queryset=Departamento.objects.all())
	tipo_aliado = forms.ModelChoiceField(label = "Tipo de Aliado", queryset = TipoAliado.objects.all().order_by('nombre'))
	
	class Meta:
		model = Aliado
		fields = ['nombre_comercial', 'razon_social','rtn_aliado', 'direccion', 'correo',
		'telefono',  'logo', 'tipo_aliado', 'rubro_aliado', 'departamento', 'municipio', 
		'aldea' ,'rsc_rse', 'rtn_fundacion', 'nombre_fundacion', 'direccion_fundacion']

		exclude = ['usuario_creador', 'usuario_modifico', 'fecha_creacion', 'fecha_modifico']

		
		#QUITAR DEPARTAMENTO ALDEA Y MUNICIPIO!!!!!!!!!!!!!!!!!!

class LogoForm(ModelForm):
	title  =  forms.CharField ( max_length = 50 ) 
	file  =  forms.FileField ()

	class Meta: 
		model = Aliado

		fields = ['logo']
		exclude = ['nombre_comercial', 'razon_social','rtn_aliado', 'direccion', 'correo',
		'telefono',  'tipo_aliado', 'rubro_aliado', 'departamento', 'municipio', 'aldea' ,'rsc_rse', 'rtn_fundacion', 'nombre_fundacion', 'direccion_fundacion']


class DirectivaFormulario(ModelForm):

	class Meta:
		model = DirectivaAliado
		exclude = ['usuario_creador', 'usuario_modifico', 'aliado', 'contacto_rsc_rse', 'contacto_primario']
	

class RubroInversionEducaForm(ModelForm):

	class Meta:
		model = RubroInversionEduca
		fields = '__all__'
		