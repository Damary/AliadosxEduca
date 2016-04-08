from django import forms
from django.forms import ModelForm
from aliado.models import Aliado

class AliadoFormulario(ModelForm):
	class Meta:
		model = Aliado
		fields = ['nombre_comercial', 'razon_social','rtn_aliado', 'rubro_aliado', 'direccion', 'correo',
		'telefono', 'departamento', 'municipio', 'aldea', 'logo', 'tipo_aliado']

class AliadoFormulario2(ModelForm):
	class Meta:
		model = Aliado
		fields = [ 'rsc_rse', 'rtn_fundacion', 'nombre_fundacion', 'direccion_fundacion']