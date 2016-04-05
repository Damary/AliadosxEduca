# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .forms import RegistroUserForm


def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUserForm(request.POST)
    else:
        form = RegistroUserForm()
    context = {'form': form }
    return render(request, 'registro.html', context)