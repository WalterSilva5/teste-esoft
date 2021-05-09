# encoding: utf-8

from app.models import Usuario
from django.shortcuts import render, redirect
from app.tests import UsuarioTest
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

usuario_test = UsuarioTest()

def cadastrar(request):
    return render(request, "cadastrar.html")
@csrf_exempt
def verifica_usuario_cadastrado(request):
    email = request.POST["email"].upper()
    if usuario_test.verificar_usuario(email, "")=="senha":
        return HttpResponse("CADASTRADO")
    else:
        return HttpResponse("NAO_CADASTRADO")

@csrf_exempt
def efetuar_cadastro(request):
    nome = request.POST["nome"].upper()
    email = request.POST["email"].upper()
    senha = request.POST["senha"]
    cep = request.POST["cep2"]
    endereco = request.POST["logradouro"].upper()
    numero = request.POST["numero"].upper()
    bairro = request.POST["bairro"].upper()
    cidade = request.POST["localidade"].upper()
    estado = request.POST["uf"].upper()
    
    #verifica se o usuario ja esta cadastrado
    if usuario_test.verificar_usuario(email, "")=="senha":
        return HttpResponse("CADASTRADO")
    else:
        usuario = Usuario(nome=nome, email=email, senha=senha, cep=cep, endereco=endereco, numero=numero, bairro=bairro, cidade=cidade, estado=estado)
        usuario.save()    # View code here...
        return HttpResponse("OK")

