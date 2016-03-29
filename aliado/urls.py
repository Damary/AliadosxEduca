from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns ('aliado.views',

	#url(r'^organizacion/', 'datos_organizacion', name='organizacion' ),

	
	url(r'^aliado/registrar/aliado', views.registrar_aliado, name='registrar_aliado'),
    
	)