from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from aliado.models import *
from . forms import *
from django.contrib.auth import authenticate, login, logout

import json
# Create your views here.



def registrar_aliado (request):

	aliado = AliadoFormulario()
	
	
	departamento = Departamento.objects.all()
	if request.method == 'GET':
		print 'departamento', departamento
		
		data = { 'departamento': departamento, 'aliado': aliado }

	return render_to_response('registrar_aliado.html', data, context_instance=RequestContext(request))


def trae_municipios (request):

	if request.method == 'GET':
		departamento = Departamento.objects.all()
		print 'dfjfdkskd', departamento, 'fdjsdfsdkj'

		if request.GET.get('bandera')== 'd':
			print 'entra a get'
			municipios = Municipio.objects.filter(departamento = request.GET['id']).order_by('codigo')
			data = [{'pk': mun.id, 'codigo': mun.codigo, 'nombre': mun.nombre} for mun in municipios] 
		else:
			data = {} 
			print 'jdfsdfhjksdfhksjdf'	
		return HttpResponse(json.dumps(data), content_type="application/json")
	else:
		return HttpResponse('noi funciono')


def trae_aldeas (request):

	if request.method == 'GET':

		print 'llega a get 9'
		if request.GET.get('bandera') == 'f':
			aldeas = Aldea.objects.filter(municipio = request.GET['id']).order_by('codigo')
			data = [{'pk': ald.id, 'codigo': ald.codigo, 'nombre': ald.nombre,  } for ald in aldeas]
		return HttpResponse(json.dumps(data), content_type="application/json")
	else:
		return HttpResponse('fallo') 


def registrar_directiva (request):
	directiva = DirectivaFormulario()

	data = {'directiva': directiva}
	 

	if request.method == 'GET':
		return render_to_response ('registrar_directiva.html', data, context_instance=RequestContext(request))
		
	else:
		return HttpResponse('hola')

def registrar_rsc_rse (request):
	aliado = AliadoFormulario()
	directiva = DirectivaFormulario()

	data = {'aliado': aliado, 'directiva':directiva}
	 

	if request.method == 'GET':
		return render_to_response ('registrar_datos_rsc_rse.html', data, context_instance=RequestContext(request))
		
	else:
		return HttpResponse('hola')

def registrar_rubros_inversion (request):

	aliado = AliadoFormulario()
	rubro = RubroInversionEducaForm()

	if request.method == 'GET':
		return render_to_response ('registrar_rubros_inversion.html', {'aliado':aliado, 'rubro':rubro }, context_instance=RequestContext(request))
		
	else:
		return HttpResponse('hola')



