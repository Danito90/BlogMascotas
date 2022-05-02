from django.shortcuts import get_object_or_404, redirect, render

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

