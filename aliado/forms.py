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
		'telefono',  'logo', 'tipo_aliado', 'rsc_rse', 'rtn_fundacion', 'nombre_fundacion', 'direccion_fundacion','departamento',
		'rubro_aliado', 'municipio', 'aldea' ]

		
		#QUITAR DEPARTAMENTO ALDEA Y MUNICIPIO!!!!!!!!!!!!!!!!!!


class DirectivaFormulario(ModelForm):

	class Meta:
		model = DirectivaAliado
		exclude = ['usuario_creador', 'usuario_modifico', 'aliado', 'contacto_rsc_rse', 'contacto_primario']
	

class RubroInversionEducaForm(ModelForm):

	class Meta:
		model = RubroInversionEduca
		fields = '__all__'
		