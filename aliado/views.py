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

# AL CREAR USUARIO SI ENCUENTRA EL RTN, GUARDA USUARIO ALIADO, Y LUEGO MANDA AL MENU, SI NO ENCUENTRA EL RTN LO MANDA DE 
#UN SOLO A REGISTRAR EL ALIADO Y HACE EL GUARDADO NORMAL Y AGREGAR EL USUARIO CREADOR A USUARIOS ALIADO, 
#AGREGAR EL GUARDADO D USUARIOSALIADO EN LA VIEW DE REGISTRAR ALIADO

class RegistroAliado(View):
	@method_decorator(login_required)
	def get(self, request):
		
		departamento = Departamento.objects.all()
		directiva = DirectivaFormulario()
		aliado = AliadoFormulario(request.POST, request.FILES)
		data = { 'departamento': departamento, 'aliado': aliado, 'directiva': directiva }
		usuarioaliado = UsuariosAliado.objects.all()
		
		#aliado = AliadoFormulario(request.POST)
		data = { 'departamento': departamento, 'aliado': aliado, 'directiva': directiva }
		return render(request,'registrar_aliado.html', data)


	@method_decorator(login_required)
	def post(self, request):
		departamento = Departamento.objects.all()
		directiva = DirectivaFormulario()
		aliado = AliadoFormulario(request.POST, request.FILES)
		comprueba = Aliado.objects.filter(rtn_aliado = request.POST.get('rtn_aliado'))
		
		data = {'departamento': departamento, 'aliado': aliado, 'directiva': directiva}
		if comprueba:
			data['error'] = u'La Empresa/Organización ya ha sido Registrada, por favor verifique su RTN'
			return render_to_response('registrar_aliado.html', data, context_instance=RequestContext(request))
			logo = Aliado(logo = request.FILES['logo'])
		else:
			try:
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
				
				registro.departamento = Departamento.objects.get( id= request.POST.get('departamento'))
				registro.municipios = Municipio.objects.get( id = request.POST.get('municipio'))
				registro.aldea = Aldea.objects.get( id= request.POST.get('aldea'))
				registro.tipo_aliado =  TipoAliado.objects.get ( id= request.POST.get('tipo_aliado'))
				registro.usuario_creador = request.user
				registro.usuario_modifico = request.user
				registro.fecha_creacion = datetime.now()
				registro.fecha_modificaciom = datetime.now()
				registro.save()

				aliado = registro
				
					
				usuario_aliado = UsuariosAliado()
				usuario_aliado.aliado = Aliado.objects.get(id = aliado.id)
				usuario_aliado.usuario = User.objects.get(id=request.user.id)
				usuario_aliado.save()
			

				gerencia = DirectivaAliado()
				gerencia.aliado = Aliado.objects.get(id= aliado.pk)
				gerencia.contacto_primario = True
				gerencia.titulo = request.POST.get('titulo_directiva')
				gerencia.nombre = request.POST.get('nombre_directiva')
				gerencia.cargo = request.POST.get('cargo_directiva')
				gerencia.correo = request.POST.get('correo_directiva')
				gerencia.telefono = request.POST.get ('telefono_directiva')
				gerencia.celular = request.POST.get('celular_directiva')
				
				gerencia.usuario_creador = request.user
				gerencia.usuario_modifico = request.user
				gerencia.fecha_creacion = datetime.now()
				gerencia.fecha_modificaciom = datetime.now()
				gerencia.save()

				#aqui va lo de usuarioaliado
							

				if request.POST.get('seleccion_rsc') == 'muestra':
					
					fundacion = Aliado()
					fundacion.aliado = Aliado.objects.get(id= aliado.id)
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

					
					contacto = DirectivaAliado()
					contacto.contacto_rsc_rse = True
					contacto.contacto_primario = False
					contacto.aliado = Aliado.objects.get(id= aliado.id)
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
					
					contacto = DirectivaAliado()
					
					contacto.contacto_rsc_rse = True
					contacto.contacto_primario = False
					contacto.aliado = Aliado.objects.get(id= aliado.id)
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
					
					
				if request.POST.get('check_secundario') == 'muestra':
								
					contacto_secundario = DirectivaAliado()
					contacto_secundario.contacto_primario = False
					contacto_secundario.aliado = Aliado.objects.get(id= aliado.id)
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
				
					
				departamento = Departamento.objects.all()
				directiva = DirectivaFormulario()
				aliado = AliadoFormulario(request.POST, request.FILES)

				#context =  {'departamento': departamento, 'aliado': aliado, 'directiva': directiva,'exito': True }
				#return render(request, 'menu_principal_aliado.html', context)
				print 'ooo'
				return HttpResponseRedirect(reverse('MenuPrincipal'))
				
			except Exception, e:
				
				error = u'Hubo un error al guardar por favor revise la información.'
				#data['error'] = u'Hubo un error al guardar por favor revise la información.'
				data =  {'departamento': departamento, 'aliado': aliado, 'directiva': directiva, 'error': error }
				return render_to_response('registrar_aliado.html', data, context_instance=RequestContext(request))

			
			return render_to_response('registrar_aliado.html', data, context_instance=RequestContext(request))
			#return HttpResponseRedirect(reverse('MenuPrincipal'))

class MenuPrincipalAliado(View):

		def get (self, request):
			
			return render(request,'menu_principal_aliado.html')

		@method_decorator(login_required)
	 	def post(self, request):
	 		
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




