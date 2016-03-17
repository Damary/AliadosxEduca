from django import forms
from django.forms import ModelForm
from .models import  *

class AliadoFormulario(forms.ModelForm):
	class Meta:
		model = Aliado #toma todos los campos del modelo organizacion
		fields = '__all__'