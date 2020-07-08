from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

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


def home_param(request, post_id):
    return HttpResponse(f"<h1>olá post id {post_id}</h1>")
