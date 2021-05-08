# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from app.models import *
# Create your tests here.

class UsuarioTest():
    def verificar_usuario(self, email, senha):
        if not (Usuario.objects.filter(email=email)):
            return "email"   
        elif not (Usuario.objects.filter(email=email, senha=senha)):
            return "senha"
        else:
            return "ok"

class ManipulaSession():
    def verifica_logado(self, request):
        try:
            email = request.session["email"]
            if request.session["email"] == "" or request.session["email"] == None:
                return False
            else:
                return True
        except:

            return False