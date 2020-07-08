from django.db import models


# ORM - relacionamento de objeto relacional
# Classe do modelo de dados
# mapear estrutura da tabela
class Post(models.Model):
    # campos do bando de dados
    # e colocando o tipo do registro através do model.
    title = models.CharField(max_length=255)  # max_length=255->maximo de caracteres
    content = models.TextField()  # TextField -> não tem limite de caractere


# após fazer alterações ou adicões no banco(
# python manage.py makemigrations my_app
# e
# python manege.py migrate my_app)

# Para saber o sql ( python manage.py sqlmigrate my_app 0001 )
