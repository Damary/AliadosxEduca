from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from . forms import *
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def sdssd(request):
	form = LoginForm()
 
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			print 'valiso'
			usuario = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=usuario, password=password)
 
			if user is not None:
				if user.is_active:
					login(request, user)
					print 'entr<'
					return HttpResponseRedirect('registrar_aliado.html')
				else:
					print 'no'
					ctx = {"form":form, "mensaje": "Usuario Inactivo"}
					return render_to_response("login.html",ctx, context_instance=RequestContext(request))
			else:
				print 'aqui'
				ctx = {"form":form, "mensaje": "Datos incorrecto"}
				return render_to_response("login.html",ctx, context_instance=RequestContext(request))	
	else:
		print 'alla'
		ctx = {'form':form}
		return render_to_response("login.html",ctx, context_instance=RequestContext(request))

 
	ctx = {"form":form, "mensaje":"hola"}
	return render_to_response("login.html",ctx, context_instance=RequestContext(request))


def registrar_aliado (request):

	aliado = AliadoFormulario()
	data = {'aliado':aliado}

	return render_to_response('registrar_aliado.html', data, context_instance=RequestContext(request))


