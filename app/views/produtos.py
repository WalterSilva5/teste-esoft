# encoding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from app.tests import ManipulaSession
from app.models import Produto
from django.views.decorators.csrf import csrf_exempt
from django.utils.formats import localize


manipula_session = ManipulaSession()

def produtos(request):
    #verifica se o usuario esta logado para poder acessar a pagina
    if manipula_session.verifica_logado(request):
        #ordena o select, tabelas com um sinal de menos são ordenadas inversamente
        #a prioridade e da esquerda para a direita para a ordenacao!
        produtos = Produto.objects.all().order_by('nome', '-preco', '-estoque')
        return render(request, 'produtos.html', {"produtos": produtos})
    else:
        return render(request, 'login.html', {"mensagem": "ERRO: NECESSARIO FAZER LOGIN!"})

def produto_cadastrado(nome):
    if(Produto.objects.filter(nome=nome)):
        return True
    
@csrf_exempt
def dados_do_produto(request):
    id = request.POST["id"]
    produto = list(Produto.objects.filter(id=id).values())[:]
    return JsonResponse({"produto": produto})

@csrf_exempt
def excluir_produto(request):
    id = request.POST["id"]
    try:
        Produto.objects.filter(id=id).delete()
        return HttpResponse("OK")
    except Exception:
        return HttpResponse("ERROR")

@csrf_exempt
def atualizar_produto(request):
    nome = request.POST["nome"].upper()
    estoque = float(request.POST["estoque"])
    preco = float(request.POST["preco"])
    id = request.POST["id"]
    
    atual = list(Produto.objects.filter(id=id).values())[0]
    existe_nome = Produto.objects.filter(nome=nome)
    if estoque < 0:
            return HttpResponse("ESTOQUE_NEGATIVO")
    elif preco < 0:
        return HttpResponse("PRECO_NEGATIVO")
    elif nome != atual["nome"]:
        if existe_nome:
            return HttpResponse("NOME_JA_CADASTRADO")
        else:
            Produto.objects.filter(id=id).update(nome=nome, preco=preco, estoque=estoque)
            return HttpResponse("OK")
    else:
        Produto.objects.filter(id=id).update(nome=nome, preco=preco, estoque=estoque)
        return HttpResponse("OK")
   
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
