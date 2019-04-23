from django.conf.urls import include, url
from . import views
from django.urls import path


urlpatterns = [
     url(r'^$', views.listarUsuarios, name="paginaprincipal"),
     #url para agregar usuarios
     url('administrador/agregarusuarios', views.AgregarUsuarios, name="agregarusuarios.adm"),
    
]