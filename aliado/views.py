# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from aliado.models import *
from . forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse, resolve
from datetime import datetime
import json
# Create your views here.


class RegistroAliado(View):
	@method_decorator(login_required)
	def get(self, request):
		print request.user, 'suarioooooooooooooooooooo'
		departamento = Departamento.objects.all()
		directiva = DirectivaFormulario()
		aliado = AliadoFormulario(request.POST, request.FILES)
		data = { 'departamento': departamento, 'aliado': aliado, 'directiva': directiva }
		print 'aja'
		print 'eje'
		#aliado = AliadoFormulario(request.POST)
		data = { 'departamento': departamento, 'aliado': aliado, 'directiva': directiva }
		return render(request,'registrar_aliado.html', data)

	@method_decorator(login_required)
	def post(self, request):
		departamento = Departamento.objects.all()
		directiva = DirectivaFormulario()
		aliado = AliadoFormulario(request.POST, request.FILES)
		comprueba = Aliado.objects.filter(rtn_aliado = request.POST.get('rtn_aliado'))
		print 'comprueba', comprueba
		data = {'departamento': departamento, 'aliado': aliado, 'directiva': directiva}
		if comprueba:
			print 'entra a error'
			data['error'] = u'La Empresa/Organización ya ha sido Registrada, por favor verifique su RTN'
			return render_to_response('registrar_aliado.html', data, context_instance=RequestContext(request))

			logo = Aliado(logo = request.FILES['logo'])
			print 'llrga llega'
		else:

			try:
				
				print request.POST.get('nombre_comercial'), request.POST.get('razon_social'), request.POST.get('rtn_aliado'), request.POST.get('rubro_aliado')
				print 'tipo_aliado: ', request.POST.get('tipo_aliado')
				registro = Aliado()
				registro.nombre_comercial =request.POST.get('nombre_comercial')
				registro.usuario_logueado = request.user
				registro.razon_social = request.POST.get('razon_social')
				registro.rtn_aliado = request.POST.get('rtn_aliado')
				registro.rubro_aliado=  RubroEmpresa.objects.get( id= request.POST.get('rubro_aliado'))
				registro.direccion = request.POST.get('direccion')
				registro.correo = request.POST.get('correo')
				registro.telefono = request.POST.get('telefono')
				
				#registro.logo = Aliado(logo = request.FILES['logo'])
				print 'prosigue', request.POST.get('departamento'), request.POST.get('municipio'), request.POST.get('aldea')
				registro.departamento = Departamento.objects.get( id= request.POST.get('departamento'))
				registro.municipios = Municipio.objects.get( id = request.POST.get('municipio'))
				registro.aldea = Aldea.objects.get( id= request.POST.get('aldea'))
				registro.tipo_aliado =  TipoAliado.objects.get ( id= request.POST.get('tipo_aliado'))
				print 'jhjsdf', registro.tipo_aliado
				registro.usuario_creador = request.user
				print 'pppppp',  registro.usuario_creador 
				registro.usuario_modifico = request.user
				registro.fecha_creacion = datetime.now()
				registro.fecha_modificaciom = datetime.now()
				print 'OOOOOOOOOOO'
				registro.save()

				aliado = registro.pk	

				print 'registro',  registro.pk	

				
				gerencia = DirectivaAliado()
				print 'entro a gerencia'
				gerencia.aliado = Aliado.objects.get(id= aliado)
				print gerencia.aliado
				gerencia.contacto_primario = True
				gerencia.titulo = request.POST.get('titulo_directiva')
				gerencia.nombre = request.POST.get('nombre_directiva')
				gerencia.cargo = request.POST.get('cargo_directiva')
				gerencia.correo = request.POST.get('correo_directiva')
				gerencia.telefono = request.POST.get ('telefono_directiva')
				gerencia.celular = request.POST.get('celular_directiva')
				print gerencia.celular
				gerencia.usuario_creador = request.user
				gerencia.usuario_modifico = request.user
				gerencia.fecha_creacion = datetime.now()
				gerencia.fecha_modificaciom = datetime.now()
				gerencia.save()
				

				if request.POST.get('radio') == 'muestra':
					print 'hola'
					fundacion = Aliado()
					fundacion.aliado = Aliado.objects.get(id= aliado)
					fundacion.rtn_fundacion = request.POST.get('rtn_fundacion')
					fundacion.nombre_fundacion = request.POST.get('nombre_fundacion')
					fundacion.direccion_fundacion = request.POST.get('direccion_fundacion')
					fundacion.rsc_rse = True
					fundacion.usuario_logueado = request.user
					fundacion.usuario_creador = request.user
					fundacion.usuario_modifico = request.user
					fundacion.fecha_creacion = datetime.now()
					fundacion.fecha_modificaciom = datetime.now()
					fundacion.save()

					print 'guardo la fundacion'
					contacto = DirectivaAliado()
					contacto.contacto_rsc_rse = True
					contacto.contacto_primario = False
					contacto.aliado = Aliado.objects.get(id= aliado)
					contacto.titulo = request.POST.get('titulo_rsc')
					contacto.nombre = request.POST.get('nombre_rsc')
					contacto.cargo = request.POST.get('cargo_rsc')
					contacto.correo = request.POST.get('correo_rsc')
					contacto.telefono = request.POST.get ('telefono_rsc')
					contacto.celular = request.POST.get('celular_rsc')
					contacto.usuario_creador = request.user
					contacto.usuario_modifico = request.user
					contacto.fecha_creacion = datetime.now()
					contacto.fecha_modificaciom = datetime.now()
					contacto.save() 
				else:
					print 'entra al else'
					contacto = DirectivaAliado()
					contacto.contacto_rsc_rse = True
					contacto.contacto_primario = False
					contacto.aliado = Aliado.objects.get(id= aliado)
					contacto.titulo = request.POST.get('titulo_rsc')
					contacto.nombre = request.POST.get('nombre_rsc')
					contacto.cargo = request.POST.get('cargo_rsc')
					contacto.correo = request.POST.get('correo_rsc')
					contacto.telefono = request.POST.get ('telefono_rsc')
					contacto.celular = request.POST.get('celular_rsc')
					contacto.usuario_creador = request.user
					contacto.usuario_modifico = request.user
					contacto.fecha_creacion = datetime.now()
					contacto.fecha_modificaciom = datetime.now()
					contacto.save() 
					print 'guardo contacto rsc/rse'


					print 'guardo contacto'
				if request.POST.get('check_secundario') == 'muestra':
					print 'byby'
					contacto_secundario = DirectivaAliado()
					contacto_secundario.contacto_primario = False
					contacto_secundario.aliado = Aliado.objects.get(id= aliado)
					contacto_secundario.titulo = request.POST.get('titulo_secundario')
					contacto_secundario.nombre = request.POST.get('nombre_secundario')
					contacto_secundario.cargo = request.POST.get('cargo_secundario')
					contacto_secundario.correo = request.POST.get('correo_secundario')
					contacto_secundario.telefono = request.POST.get ('telefono_secundario')
					contacto_secundario.celular = request.POST.get('celular_secundario')
					contacto_secundario.usuario_creador = request.user
					contacto_secundario.usuario_modifico = request.user
					contacto_secundario.fecha_creacion = datetime.now()
					contacto_secundario.fecha_modificaciom = datetime.now()
					contacto_secundario.save() 
					print 'fin fin'

				print 'llego para menu principal'
				departamento = Departamento.objects.all()
				directiva = DirectivaFormulario()
				aliado = AliadoFormulario(request.POST, request.FILES)

				data =  {'exito': True }
				print 'redirige a menu principal'
				return render('menu_principal_aliado.html', data)


			except Exception, e:
				print e, 'llego en el error'
				error = u'Hubo un error al guardar por favor revise la información.'
				#data['error'] = u'Hubo un error al guardar por favor revise la información.'
				data =  {'departamento': departamento, 'aliado': aliado, 'directiva': directiva, 'error': error }
				return render_to_response('registrar_aliado.html', data, context_instance=RequestContext(request))

			print 'llego para menu principal final'
			return render_to_response('registrar_aliado.html', data, context_instance=RequestContext(request))
			#return HttpResponseRedirect(reverse('MenuPrincipal'))

class MenuPrincipalAliado(View):

		def get (self, request):
			print 'gueteo'
			return render(request,'menu_principal_aliado.html')

		@method_decorator(login_required)
	 	def post(self, request):
	 		print 'llego al post del menu principal'
	 		return render(request,'menu_principal_aliado.html')


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



