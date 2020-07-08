from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

# MVC - Model View Controller
# M - models.py
# V - html
# C - views.py

# MTV
# M models.py
# T template
# V views.py


def home(request):
    return HttpResponse('<h1>Olá, mundo</h1>')


def post(request, post_id):
    posts = Post.objects.get(id=post_id)
    return render(request, 'post.html', {'post':posts})


def post_list(request):
    posts = Post.objects.all()

    return render(request, 'post_list.html', {'posts':posts})

    # name = 'luiz Carlos'
    # return render(request, 'post_list.html', {'name': name})
    # retornando para o templates a variavel name
