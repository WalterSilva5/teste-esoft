# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
#$ python manage.py sqlmigrate polls 0001

class Usuario(models.Model):
    nome = models.CharField("nome",max_length=200, null=False)
    email = models.CharField("email",max_length=250, null=False, unique=True)
    senha = models.CharField("senha",max_length=250, null=False)
    cep = models.CharField("cep",max_length=250, null=False)
    endereco = models.CharField("endereco",max_length=250, null=False)
    numero = models.CharField("numero",max_length=250, null=False)
    bairro = models.CharField("bairro",max_length=250, null=False)
    cidade = models.CharField("cidade",max_length=250, null=False)
    estado = models.CharField("estado",max_length=250, null=False)
class Produto(models.Model):
    nome = models.CharField("nome",max_length=250, null=False, unique=True)
    estoque = models.DecimalField("estoque", blank=True, null=False, max_digits=20,  decimal_places=10)
    preco = models.DecimalField("preco", blank=True, null=False, max_digits=20,  decimal_places=10)