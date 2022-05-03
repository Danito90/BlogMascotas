from datetime import date
from django.shortcuts import get_object_or_404, redirect, render
from autores.models import Autor

from posts.models import Post
from posts.forms import postForm


def detallePost(request):
    post = get_object_or_404(Post, id=id)
    return render(request, 'detalle_post.html', {'detallePost': post})


def agregarPost(request):
    if request.method == 'POST':
        FormPost = postForm(request.POST)
        if FormPost.is_valid():
            FormPost.save()
            return redirect("agregarPost")
    else:
        FormPost = postForm()
    return render(request, 'form_post.html', {'FormPost': FormPost})


def actualizarPost(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        FormPost = postForm(request.POST, instance=post)
        if FormPost.is_valid():
            FormPost.save()
            return redirect("detallePost")
    else:
        FormPost = postForm(instance=post)
    return render(request, 'detalle_post.html', {'FormPost': FormPost})

def eliminarPost(request,id):
    post = get_object_or_404(Post, id=id)
    if post:
        post.delete()
    return redirect('agregarPost')

def index(request):
    nroPosts = Post.objects.filter(activo=True,reencuentro=False).count()  # cuenta cheques pagados
    posts = Post.objects.all().order_by('fecha')
    logeado = Autor.objects.filter(user=request.user.id)
    for l in logeado:
        url = l.foto.url
    # .filter(empresa__user__id=request.user.id) filtro por empresa-usuario-usuario logeado
    #.filter(empresa__user__id=1) filtra por usuario id 1
    #filtra empresa 1 -2  ... .filter(empresa__in=[1, 2,])
    vto = date.today()

    return render(request, 'index.html',{'posts': posts, 'nroPosts': nroPosts, 'vto': vto, 'url': url})