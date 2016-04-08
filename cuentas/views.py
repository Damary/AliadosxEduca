# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from .forms import RegistroUserForm
from .models import PerfilUsuario


def registro_usuario(request):
    if request.method == 'POST':
        # Si el method es post, obtenemos los datos del formulario
        form = RegistroUserForm(request.POST, request.FILES)

        # Comprobamos si el formulario es valido
        if form.is_valid():
            # En caso de ser valido, obtenemos los datos del formulario.
            # form.cleaned_data obtiene los datos limpios y los pone en un
            # diccionario con pares clave/valor, donde clave es el nombre del campo
            # del formulario y el valor es el valor si existe.
            cleaned_data = form.cleaned_data
            usuario = cleaned_data.get('usuario')
            password = cleaned_data.get('password')
            email = cleaned_data.get('email')
            
            # E instanciamos un objeto User, con el username y password
            user_model = User.objects.create_user(username=usuario, password=password)
            # Añadimos el email
            user_model.email = email
            # Y guardamos el objeto, esto guardara los datos en la db.
            user_model.save()
            # Ahora, creamos un objeto UserProfile, aunque no haya incluido
            # una imagen, ya quedara la referencia creada en la db.
            user_profile = UserProfile()
            # Al campo user le asignamos el objeto user_model
            user_profile.user = user_model
            
            # Por ultimo, guardamos tambien el objeto UserProfile
            user_profile.save()
            # Ahora, redireccionamos a la pagina cuentas/gracias.html
            # Pero lo hacemos con un redirect.
            print 'oiuewruierwre'
            #return redirect(reverse('cuentas.gracias', kwargs={'username': username}))
    else:
        # Si el mthod es GET, instanciamos un objeto RegistroUserForm vacio
        print  'errorrrrrrrrrrrrrrrrrrrrrrrrrrrr'
        form = RegistroUserForm()
    # Creamos el contexto
    context = {'form': form}
    # Y mostramos los datos
    return render(request, 'registro.html', context)


def clean(self):
   if 'password' in self.cleaned_data and 'password1' in self.cleaned_data and self.cleaned_data['password'] != self.cleaned_data['password1']:
       raise forms.ValidationError("The password does not match ")
   return self.cleaned_data