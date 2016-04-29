# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from aliado.models import *
from . forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import json
# Create your views here.


@login_required
def registrar_aliado (request):

	print request.user, 'suarioooooooooooooooooooo'
	departamento = Departamento.objects.all()
	directiva = DirectivaFormulario()
	aliado = AliadoFormulario(request.POST, request.FILES)
	data = { 'departamento': departamento, 'aliado': aliado, 'directiva': directiva }
	print 'aja'
	if request.method == 'POST':

		comprueba = Aliado.objects.filter(rtn_aliado = request.POST.get('rtn_aliado'))
		print 'comprueba', comprueba
		if comprueba:
			print 'entra a error'
			data['error'] = u'La Empresa/Organización ya ha sido Registrada, por favor verifique su RTN'
			return render_to_response('registrar_aliado.html', data, context_instance=RequestContext(request))

			logo = Aliado(logo = request.FILES['logo'])
			print 'llrga llega'
		else:

			print request.POST.get('nombre_comercial'), request.POST.get('razon_social'), request.POST.get('rtn_aliado'), request.POST.get('rubro_aliado')
			print 'tipo_aliado: ', request.POST.get('tipo_aliado')
			registro = Aliado()
			registro.nombre_comercial =request.POST.get('nombre_comercial')
			registro.razon_social = request.POST.get('razon_social')
			registro.rtn_aliado = request.POST.get('rtn_aliado')
			registro.rubro_aliado=  RubroEmpresa.objects.get( id= request.POST.get('rubro_aliado'))
			registro.direccion = request.POST.get('direccion')
			registro.correo = request.POST.get('correo')
			registro.telefono = request.POST.get('telefono')
			print 'aja'
			#registro.logo = Aliado(logo = request.FILES['logo'])
			print 'prosigue', request.POST.get('departamento'), request.POST.get('municipio'), request.POST.get('aldea')
			registro.departamento = Departamento.objects.get( id= request.POST.get('departamento'))
			registro.municipios = Municipio.objects.get( id = request.POST.get('municipio'))
			registro.aldea = Aldea.objects.get( id= request.POST.get('aldea'))
			registro.tipo_aliado =  TipoAliado.objects.get ( id= request.POST.get('tipo_aliado'))
			registro.usuario_creador = request.user
			registro.usuario_modifico = request.user
			registro.save()
			print 'ufffffff todo'
			data =  {'departamento': departamento, 'aliado': aliado, 'directiva': directiva, 'exito': True }
			return render_to_response('registrar_aliado.html', data, context_instance=RequestContext(request))


	elif request.method == 'GET':
		print 'eje'
		aliado = AliadoFormulario(request.POST)
		data = { 'departamento': departamento, 'aliado': aliado, 'directiva': directiva }
	
				
		

	return render_to_response('registrar_aliado.html', data, context_instance=RequestContext(request))


def trae_municipios (request):

	if request.method == 'GET':
		departamento = Departamento.objects.all()
		
		if request.GET.get('bandera')== 'd':
			
			municipios = Municipio.objects.filter(departamento = request.GET['id']).order_by('codigo')
			data = [{'pk': mun.id, 'codigo': mun.codigo, 'nombre': mun.nombre} for mun in municipios] 
		else:
			data = {} 
			
		return HttpResponse(json.dumps(data), content_type="application/json")
	else:
		return HttpResponse('noi funciono')


def trae_aldeas (request):

	if request.method == 'GET':

		if request.GET.get('bandera') == 'f':
			aldeas = Aldea.objects.filter(municipio = request.GET['id']).order_by('codigo')
			data = [{'pk': ald.id, 'codigo': ald.codigo, 'nombre': ald.nombre,  } for ald in aldeas]
		return HttpResponse(json.dumps(data), content_type="application/json")
	else:
		return HttpResponse('fallo') 


# def registrar_directiva (request):
# 	directiva = DirectivaFormulario()

# 	data = {'directiva': directiva}
	 

# 	if request.method == 'GET':
# 		return render_to_response ('registrar_directiva.html', data, context_instance=RequestContext(request))
		
# 	else:
# 		return HttpResponse('hola')

# def registrar_rsc_rse (request):
# 	aliado = AliadoFormulario()
# 	directiva = DirectivaFormulario()

# 	data = {'aliado': aliado, 'directiva':directiva}
	 

# 	if request.method == 'GET':
# 		return render_to_response ('registrar_datos_rsc_rse.html', data, context_instance=RequestContext(request))
		
# 	else:
# 		return HttpResponse('hola')

# def registrar_rubros_inversion (request):

# 	aliado = AliadoFormulario()
# 	rubro = RubroInversionEducaForm()

# 	if request.method == 'GET':
# 		return render_to_response ('registrar_rubros_inversion.html', {'aliado':aliado, 'rubro':rubro }, context_instance=RequestContext(request))
		
# 	else:
# 		return HttpResponse('hola')



