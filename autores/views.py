from django.shortcuts import get_object_or_404, redirect, render

from autores.models import Autor
from autores.forms import autorForm

def detalleAutor(request,id):
    autor = get_object_or_404(Autor,id=id)
    return render(request, 'detalle_autor.html', {'detalleAutor': autor})
    

def agregarAutor(request):
    if request.method == 'POST':
        FormAutor = autorForm(request.POST)  # obtenemos los datos del formulario
        if FormAutor.is_valid():
            FormAutor.save()
            return redirect("agregarAutor")  # volvemos a la misma pagina pasamos el parametro y enviamos mensaje
    else:
        FormAutor = autorForm()
    return render(request, 'form_autor.html', {'FormAutor': FormAutor})

def actualizarAutor(request,id):
    autor = get_object_or_404(Autor,id=id)
    if request.method == 'POST':
        FormAutor=autorForm(request.POST,instance=autor)
        if FormAutor.is_valid():
           FormAutor.save()
           return redirect("detalleAutor")
    else:
         FormAutor=autorForm(instance=autor)
    return render(request, 'detalle_autor.html', {'FormAutor': FormAutor})

def eliminarAutor(request,id):
    autor = get_object_or_404(Autor,id=id)
    if autor:
        autor.delete()
    return redirect("agregarAutor")