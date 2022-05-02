from django.shortcuts import get_object_or_404, redirect, render
from contactos.models import Contacto
from contactos.forms import contactoForm

def detalleContacto(request):
    contacto= get_object_or_404(Contacto,id=id)
    return render(request, 'detalle_contacto.html', {'detalleContacto': contacto})

def agregarContacto(request):
    if request.method == 'POST':
        FormContacto = contactoForm(request.POST)
        if FormContacto.is_valid():
            FormContacto.save()
            return redirect("agregarContacto")
    else:
        FormContacto = contactoForm()
    return render(request, 'form_contacto.html', {'FormContacto': FormContacto})

def actualizarContacto(request,id):
    contacto = get_object_or_404(Contacto,id=id)
    if request.method == 'POST':
        FormContacto = contactoForm(request.POST,instance=contacto)
        if FormContacto.is_valid():
            FormContacto.save()
    else:
        FormContacto = contactoForm(instance=contacto)
    return render(request, 'detalle_contacto.html', {'FormContacto': FormContacto})

def eliminarContacto(request,id):
    contacto = get_object_or_404(Contacto,id=id)
    if contacto:
        contacto.delete()
    return redirect("agregarContacto")