# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from aliadosxeducacion.forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

def login_page(request):

	message= None 
	form = LoginForm(request.POST)
	
	if request.method == "POST":
		form = LoginForm(request.POST)
		error ={}
		if form.is_valid():
			userame = request.POST['username']
			password = request.POST.get('password')
			user = authenticate(username=username, password=password)
			if  user is not None:
				if user.is_active:
					login(request, user)
					message = ("Bienvenido")
					return HttpResponseRedirect('aliado/registrar/aliado/')
				else:
					message = "Usuario Inactivo"
			else:
				message = "Nombre de Usuario y/o Contraseña equivocados"
		else:
			return render_to_response( 'login.html', {'message':message, 'form':form}, context_instance = RequestContext(request))
	elif request.method == "GET":
		form = LoginForm()
		return render_to_response( 'login.html', {'message':message, 'form':form}, context_instance = RequestContext(request))
	return render_to_response( 'login.html', {'message':message, 'form':form}, context_instance = RequestContext(request))