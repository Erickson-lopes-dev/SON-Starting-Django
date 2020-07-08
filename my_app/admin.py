from django.contrib import admin

from .models import Post, Category

# Adicionando visualização do modelo de dados criada
admin.site.register(Post)
admin.site.register(Category)

