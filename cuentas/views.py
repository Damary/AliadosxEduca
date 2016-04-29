# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from .forms import UserProfile
from .models import PerfilUsuario




def registro_usuario(request):
    if request.method == 'POST':
        print 'entra aqui'
        # Si el method es post, obtenemos los datos del formulario
        form = UserProfile(request.POST, request.FILES)

        # Comprobamos si el formulario es valido
        if form.is_valid():
            # En caso de ser valido, obtenemos los datos del formulario.
            # form.cleaned_data obtiene los datos limpios y los pone en un
            # diccionario con pares clave/valor, donde clave es el nombre del campo
            # del formulario y el valor es el valor si existe.
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            password = cleaned_data.get('password')
            email = cleaned_data.get('email')
            nombre = cleaned_data.get('nombre')
            apellido= cleaned_data.get ('apellido')
            print username, password, email, nombre, apellido, '!!!!!!!!'
            
            # E instanciamos un objeto User, con el username y password
            user_model = User.objects.create_user(username=username, password=password, first_name=nombre, last_name=apellido, email=email)
            # Añadimos el email
            user_model.email = email
            user_model.first_name = nombre
            user_model.last_name = apellido
            # Y guardamos el objeto, esto guardara los datos en la db.
            user_model.save()
            # Ahora, creamos un objeto UserProfile, aunque no haya incluido
            # una imagen, ya quedara la referencia creada en la db.
            user_profile = PerfilUsuario()
            # Al campo user le asignamos el objeto user_model
            user_profile.user = user_model
            
            # Por ultimo, guardamos tambien el objeto UserProfile
            user_profile.save()
            # Ahora, redireccionamos a la pagina cuentas/gracias.html
            # Pero lo hacemos con un redirect.
            print 'oiuewruierwre'
            return HttpResponseRedirect(reverse('login'))
            
    else:
        # Si el mthod es GET, instanciamos un objeto RegistroUserForm vacio
        print  'errorrrrrrrrrrrrrrrrrrrrrrrrrrrr'
        form = UserProfile()
    # Creamos el contexto
    context = {'form': form}
    # Y mostramos los datos
    return render(request, 'registro.html', context)


def clean(self):
   if 'password' in self.cleaned_data and 'password1' in self.cleaned_data and self.cleaned_data['password'] != self.cleaned_data['password1']:
       raise forms.ValidationError("The password does not match ")
   return self.cleaned_data