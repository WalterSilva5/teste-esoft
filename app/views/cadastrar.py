from app.models import Usuario
from django.shortcuts import render
from app.tests import UsuarioTest

usuario_test = UsuarioTest()

def cadastrar(request):
    return render(request, 'cadastrar.html')

def efetuar_cadastro(request):
    #verifica se o usuario ja esta cadastrado
    if not usuario_test.verificar_usuario(request.POST["email"], "") =="email":
        return render(request, "cadastrar.html", {"mensagem": '<h2 class="mt-4 bg-warning text-danger font-weight-bold rounded">ERRO: USUARIO JA ESTA CADASTRADO!</h2>'})
    else:
        nome = request.POST["nome"]
        email = request.POST["email"]
        senha = request.POST["senha"]
        cep = request.POST["cep2"]
        endereco = request.POST["logradouro"]
        numero = request.POST["numero"]
        bairro = request.POST["bairro"]
        cidade = request.POST["localidade"]
        estado = request.POST["uf"]
        
        usuario = Usuario(nome=nome, email=email, senha=senha, cep=cep, endereco=endereco, numero=numero, bairro=bairro, cidade=cidade, estado=estado)
        usuario.save()
        return render(request, "cadastrar.html", {"mensagem": '<h2 class="mt-4 bg-primary text-light font-weight-bold rounded">CADASTRO EFETUADO COM SUCESSO!</h2>'})