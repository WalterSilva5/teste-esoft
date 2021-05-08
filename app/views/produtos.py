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
        produtos = list(Produto.objects.all().values())[:]
        print(produtos)
        return render(request, 'produtos.html', {"produtos": produtos})
    else:
        return render(request, 'login.html', {"mensagem": "ERRO: NECESSARIO FAZER LOGIN!"})

def produto_cadastrado(nome):
    if(Produto.objects.filter(nome=nome)):
        return True
    
@csrf_exempt
def cadastrar_produto(request):
    nome = request.POST["nome"].upper()
    estoque = float(request.POST["estoque"])
    preco = float(request.POST["preco"])

    
    if produto_cadastrado(nome):
        return  HttpResponse("PRODUTO_JA_CADASTRADO")
    elif estoque < 0:
        return HttpResponse("ESTOQUE_NEGATIVO")
    elif preco < 0:
        return HttpResponse("PRECO_NEGATIVO")
    else:
        produto = Produto(nome=nome, estoque=estoque, preco=preco)
        produto.save()
        return HttpResponse("OK")
