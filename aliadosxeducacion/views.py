# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from aliadosxeducacion.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.template.loader import get_template
from aliado.models import UsuariosAliado

def login_page(request):

	message= None 
	form = LoginForm(request.POST)
	
	if request.method == "POST":
		form = LoginForm(request.POST)
		error ={}
		if form.is_valid():
			print 'valido'
			username = request.POST['username']
			password = request.POST.get('clave')
			print 'username', username, 'password', password
			user = authenticate(username=username, password=password)
			
			if  user is not None:
				try:
					if user.is_active: 
						login(request, user)
						
						aliado = UsuariosAliado.objects.filter(usuario=user.id)
						
						if aliado:
							print 'verdadero'
							return render(request, 'menu_principal_aliado.html')
						else:
							print 'retorna'
							return HttpResponseRedirect('aliado/registrar/aliado/')
					else:
						
						message = "Usuario Inactivo"
				except Exception, e:
					print 'error:', e
					message= ("Error del Sistema") 

					return render_to_response( 'login.html', {'message':message, 'form':form}, context_instance = RequestContext(request))
					
			else:
				message = "Nombre de Usuario y/o Contraseña equivocados"
		else:
			print 'else'
			return render_to_response( 'login.html', {'message':message, 'form':form}, context_instance = RequestContext(request))
	elif request.method == "GET":
		form = LoginForm()
		return render_to_response( 'login.html', {'message':message, 'form':form}, context_instance = RequestContext(request))
	return render_to_response( 'login.html', {'message':message, 'form':form}, context_instance = RequestContext(request))

#@login_required(login_url = '/login')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')