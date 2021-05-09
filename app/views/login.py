from django.shortcuts import render
from app.models import Usuario
from app.tests import UsuarioTest
from app.models import Produto

usuario_test = UsuarioTest()
def login(request):
    return render(request, 'login.html')

def efetuar_login(request):
    email = request.POST["email"].upper()
    senha = request.POST["senha"].upper()
    
    verifica = usuario_test.verificar_usuario(email, senha)
    
    if verifica == "email":
        return render(request, "login.html", {"mensagem": "ERRO: EMAIL INVALIDO!"})
    elif verifica =="senha":
        return render(request, "login.html", {"mensagem": "ERRO: SENHA INCORRETA!"})
    else:
        request.session["email"] = request.POST["email"]
        produtos = Produto.objects.all().count()
        return render(request, 'home.html',{"quantidade": produtos})
def sair(request):
    try:
        request.session.flush()
    except Exception:
        pass
    return render(request, "index.html")