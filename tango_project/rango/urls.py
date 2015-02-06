from django.conf.urls import patterns, url
from rango import views
from rango import about

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'), #Esta direccion por ser la principal esta vacia 
        									   #para dejar que el archivo urls del tango_project adiministre.
        url(r'^about/', about.index, name='index')) #Asi se enrutan las urls para las distintas 
													#vistas de la aplicacion ip:port/rango/about