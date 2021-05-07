from django.shortcuts import render
from app.models import Usuario
from app.tests import UsuarioTest

usuario_test = UsuarioTest()
def login(request):
    return render(request, 'login.html')

def efetuar_login(request):
    email = request.POST["email"]
    senha = request.POST["senha"]
    
    verifica = usuario_test.verificar_usuario(email, senha)
    
    if verifica == "email":
        return render(request, "login.html", {"mensagem": "ERRO: EMAIL INVALIDO!"})
    elif verifica =="senha":
        return render(request, "login.html", {"mensagem": "ERRO: SENHA INCORRETA!"})
    else:
        return render(request, "home.html")