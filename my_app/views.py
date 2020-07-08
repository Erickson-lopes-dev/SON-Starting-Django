from django.shortcuts import render
from django.http import HttpResponse

from .models import Post, Category

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
    # procura o id dentro do DB

    posts = Post.objects.get(id=post_id)
    categories = Category.objects.all()
    return render(request, 'post.html',
                  {
                      'post': posts,
                      'categories':categories
                  })


def post_list(request):
    # verifica se a requisição vem com 'category_id'
    if 'category_id' in request.GET:
        # busca os post que tenha o id da categoria
        category = Category.objects.get(id=request.GET['category_id'])
        # filtra todos os post que tenha essa categoria
        posts = Post.objects.filter(categories=category)
    else:
        # caso nao venha retorna todos os posts
        posts = Post.objects.all()
    # procura todas as categorias
    categories = Category.objects.all()

    return render(request, 'post_list.html',
                  {
                      'posts': posts,
                      'categories': categories
                  })

    # name = 'luiz Carlos'
    # return render(request, 'post_list.html', {'name': name})
    # retornando para o templates a variavel name
