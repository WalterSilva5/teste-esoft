from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from app.tests import ManipulaSession
from app.models import Produto
from django.views.decorators.csrf import csrf_exempt


manipula_session = ManipulaSession()

def produtos(request):
    #verifica se o usuario esta logado para poder acessar a pagina
    if manipula_session.verifica_logado(request):
        return render(request, 'produtos.html')
    else:
        return render(request, 'login.html', {"mensagem": "ERRO: NECESSARIO FAZER LOGIN!"})

def produto_cadastrado(nome):
    if(Produto.objects.filter(nome=nome)):
        return True
    
@csrf_exempt
def cadastrar_produto(request):
    nome = request.POST["nome"]
    if produto_cadastrado(nome):
        return  HttpResponse(True)
    else:
        produto = Produto(nome = request.POST["nome"].upper(), estoque = request.POST["estoque"], preco = request.POST["preco"])
        produto.save()
        return HttpResponse(False)