from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic.base import TemplateView
from django.contrib.auth.views import login

urlpatterns = [
    # Examples:
    # url(r'^$', 'aliadosxeducacion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^$', TemplateView.as_view(template_name="login.html"), name="login"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('aliado.urls')),

    
]
