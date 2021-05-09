from django.shortcuts import render
from app.tests import ManipulaSession
from app.models import Produto
manipula_session = ManipulaSession()

def home(request):
    #verifica se o usuario esta logado para poder acessar a pagina
    if manipula_session.verifica_logado(request):
        produtos = Produto.objects.all().count()
        return render(request, 'home.html',{"quantidade": produtos})
    else:
        return render(request, 'login.html', {"mensagem": "ERRO: NECESSARIO FAZER LOGIN!"})