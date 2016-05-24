# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from aliado.models import *
from . forms import *
from django.template import RequestContext




def registro_usuario(request):
    if request.method == 'POST':
        departamento = Departamento.objects.all()
        directiva = DirectivaFormulario()
        aliado = AliadoFormulario(request.POST, request.FILES)
        data = { 'departamento': departamento, 'aliado': aliado, 'directiva': directiva }

        print 'entra aqui'
        # Si el method es post, obtenemos los datos del formulario
        form = UserProfile(request.POST, request.FILES)

        # Comprobamos si el formulario es valido
        if form.is_valid():
            # En caso de ser valido, obtenemos los datos del formulario.
            # form.cleaned_data obtiene los datos limpios y los pone en un
            # diccionario con pares clave/valor, donde clave es el nombre del campo
            # del formulario y el valor es el valor si existe.
    
            rtnempresa = Aliado.objects.filter(rtn_aliado = request.POST.get('rtn_aliado'))
                        
            print 'dfasdasd', rtnempresa
            try:
                print 'entra try'
                if rtnempresa:
                   
                   return HttpResponseRedirect(reverse('MenuPrincipal')) 
                else:
                
                    return HttpResponseRedirect(reverse('RegistroAliado'))
                 
                    
             
            except Exception, e:
                print 'erp<zx<zx<zx', e
            
 
            
    else:
        # Si el mthod es GET, instanciamos un objeto RegistroUserForm vacio
        print  'GET'
        form = UserProfile()
    # Creamos el contexto
    context = {'form': form}
    # Y mostramos los datos
    return render(request, 'registro.html', context)


def clean(self):
   if 'password' in self.cleaned_data and 'password1' in self.cleaned_data and self.cleaned_data['password'] != self.cleaned_data['password1']:
       raise forms.ValidationError("The password does not match ")
   return self.cleaned_data