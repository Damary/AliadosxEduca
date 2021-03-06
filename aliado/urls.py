from django.conf.urls import patterns, include, url
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = patterns ('aliado.views',

	#url(r'^organizacion/', 'datos_organizacion', name='organizacion' ),
	url(r'^aliado/registrar/aliado', login_required(views.RegistroAliado.as_view()), name='RegistroAliado'),
	url(r'^aliado/menu/principal', login_required(views.MenuPrincipalAliado.as_view()), name='MenuPrincipal'),
	url(r'^aliado/trae_municipios', views.trae_municipios, name='trae_municipios'),
	url(r'^aliado/trae_aldeas', views.trae_aldeas, name='trae_aldeas'),
	# url(r'^aliado/registrar/directiva', views.registrar_directiva, name='registrar_directiva'),
	# url(r'^aliado/registrar/rsc_rse', views.registrar_rsc_rse, name='registrar_rsc_rse'),
	# url(r'^aliado/registrar/rubros_inversion', views.registrar_rubros_inversion, name='registrar_rubros_inversion'),
	)

