from django.shortcuts import render
from app.tests import ManipulaSession

manipula_session = ManipulaSession()

def produtos(request):
    #verifica se o usuario esta logado para poder acessar a pagina
    if manipula_session.verifica_logado(request):
        return render(request, 'produtos.html')
    else:
        return render(request, 'login.html', {"mensagem": "ERRO: NECESSARIO FAZER LOGIN!"})