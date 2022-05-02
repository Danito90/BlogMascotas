from django.shortcuts import get_object_or_404, redirect, render

from mascotas.models import Mascota
from mascotas.forms import mascotaForm


def detalleMascota(request):
    mascota = get_object_or_404(Mascota, id=id)
    return render(request, 'detalle_mascota.html', {'detalleMascota': mascota})


def agregarMascota(request):
    if request.method == 'POST':
        FormMascota = mascotaForm(request.POST)
        if FormMascota.is_valid():
            FormMascota.save()
            return redirect("agregarMascota")
    else:
        FormMascota = mascotaForm()
    return render(request, 'form_mascota.html', {'FormMascota': FormMascota})


def actualizarMascota(request, id):
    mascota = get_object_or_404(Mascota, id=id)
    if request.method == 'POST':
        FormMascota = mascotaForm(request.POST, instance=mascota)
        if FormMascota.is_valid():
            FormMascota.save()
            return redirect("detalleMascota")
    else:
        FormMascota = mascotaForm(instance=mascota)
    return render(request, 'detalle_mascota.html', {'FormMascota': FormMascota})

def eliminarMascota(request,id):
    mascota = get_object_or_404(Mascota, id=id)
    if mascota:
        mascota.delete()
    return redirect('agregarMascota')
