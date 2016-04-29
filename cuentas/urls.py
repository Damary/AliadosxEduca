from django.conf.urls import url

from . import views

urlpatterns = [

	url(r'^clean/$', views.clean, name='clean'),
    url(r'^registro/$', views.registro_usuario, name='registro_usuario'),
]