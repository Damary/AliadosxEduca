from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic.base import TemplateView
from django.contrib.auth.views import login

urlpatterns = [
    # Examples:
    # url(r'^$', 'aliadosxeducacion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


   # url(r'^login/$', 'django.contrib.auth.views.login'),
   	url(r'^$', 'aliadosxeducacion.views.login_page', name="login"),
   	#url(r'^accounts/login/$', 'aliadosxeducacion.views.login_page', name="login2"), #Hace que si el usuario no esta logueado lo redirija al login 
   	url(r'^logout/$', 'aliadosxeducacion.views.logout_view', name="logout"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('aliado.urls')),
    url(r'^cuentas/', include('cuentas.urls')),

    
]
