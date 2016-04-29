# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from aliadosxeducacion.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

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
			print  user is not None, 'none', user
			if  user is not None:
				print 'None'
				if user.is_active:
					print 'active'
					login(request, user)
					message = ("Bienvenido")
					return HttpResponseRedirect('aliado/registrar/aliado/')
				else:
					message = "Usuario Inactivo"
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