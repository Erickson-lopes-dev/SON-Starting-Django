from django.db import models
from django.contrib.auth.models import User

# ORM - relacionamento de objeto relacional
# Classe do modelo de dados
# mapear estrutura da tabela
class Post(models.Model):
    # campos do bando de dados
    # e colocando o tipo do registro através do model.
    title = models.CharField(max_length=255, verbose_name='Título')  # max_length=255->maximo de caracteres
    content = models.TextField(verbose_name='Corpo do Artigo')  # TextField -> não tem limite de caractere
    # null para DB
    # blank para formulário
    subtitle = models.CharField(max_length=255, blank=True, null=True, verbose_name='Subtitulo')
    # gerando chave a partir do usuario que estiver logado
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Autor')
    # models.CASCADE -> se o usuario for deletado sera excluido o registro associado
    # PROTECT -> se o usuario for deletado não sera excluido o registro associado
    # SET_NULL -> coloca o valor nulo na chave estrangeira (precisa habilitar null=True para isso acontecer)

    class Meta:
        # mudar "post" para artigos
        verbose_name = 'Artigo'
        # caso o queira mudar o nome quando for plural
        # verbose_name_plural = 'Artigos'

    def __str__(self):
        return self.title
# após fazer alterações ou adicões no banco(
# python manage.py makemigrations my_app
# e
# python manege.py migrate my_app)

# Para saber o sql ( python manage.py sqlmigrate my_app 0001 )
# para ver as migrações e qual esta ativada (python manage.py showmigrations)
