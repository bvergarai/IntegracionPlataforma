from django.shortcuts import render, get_object_or_404
from .models import RegistrarUsuarios
from django.utils import timezone
#importar formularios
from .forms import RegistroUsuarios_form
# importamos opciones para redirigir 
from django.shortcuts import redirect

#definimos la vista para listar usuarios
def listarUsuarios(request):
    usuarios = RegistrarUsuarios.objects.all
    return render(request, 'Basural/listar_usuarios.html', {'usuarios': usuarios})

#definimos la vista para agregar usuarios
def AgregarUsuarios(request):
   if request.method == "POST":
       form = RegistroUsuarios_form(request.POST or None, request.FILES or None)
       if form.is_valid():
           post = form.save(commit=False)
           post.save()
           return redirect('paginaprincipal')
   else:
       form = RegistroUsuarios_form()
   return render(request, 'Basural/agregar_usuarios.html', {'form': form})
