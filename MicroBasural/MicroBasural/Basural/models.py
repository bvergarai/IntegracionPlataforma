from django.db import models
#Permisos DJANGO 
from django.utils.translation import ugettext as _


#Tabla usuarios 
class RegistrarUsuarios (models.Model):
    Rut = models.CharField(primary_key=True, max_length=10)
    PrimerNombre = models.CharField(max_length=200, blank=False, null=False)
    PrimerApellido = models.CharField(max_length=200, blank=False, null=False)
    Direccion = models.CharField(max_length=200, blank=False, null=False)
    Correo = models.EmailField(blank=False, null=False)

    def _str_(self):
        return self.Rut

   
     


