from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from . forms import *

# Create your views here.

def login (request):
	
	if request.method == 'GET':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None and user.is_active:
			#auth.login(request, user)
			return HttpResponseRedirect ("login.html")
			print("User is valid, active and authenticated")
		else:
			print("The username and password were incorrect.")
			return HttpResponseRedirect ("login.html")
	render_to_response ('login.html', context_instance=RequestContext(request))


def registrar_aliado (request):

	aliado = AliadoFormulario()
	data = {'aliado':aliado}

	return render_to_response('registrar_aliado.html', data, context_instance=RequestContext(request))


