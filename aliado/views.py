from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from . forms import *

# Create your views here.

def registrar_aliado (request):

	aliado = AliadoFormulario()
	data = {'aliado':aliado}

	return render_to_response('registrar_aliado.html', data, context_instance=RequestContext(request))


