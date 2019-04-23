from django import forms
# Importamos el Modelo RegistroUsuario
from .models import RegistrarUsuarios
from django.conf import settings


#creacion de formularios


#formulario registro usuario
class RegistroUsuarios_form(forms.ModelForm):
	class Meta:
		model = RegistrarUsuarios
		fields = ('Rut', 'PrimerNombre', 'PrimerApellido', 'Direccion', 'Correo')