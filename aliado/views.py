from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from aliado.models import *
from . forms import AliadoFormulario, AliadoFormulario2
from django.contrib.auth import authenticate, login, logout
# Create your views here.



def registrar_aliado (request):

	aliado = AliadoFormulario()
	alia2= AliadoFormulario2()
	
	

	if request.method == 'GET':
		data = {'aliado':aliado,  }

	return render_to_response('registrar_aliado.html', data, context_instance=RequestContext(request))


