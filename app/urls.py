from django.conf.urls import url

from app.views.views import *

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^login/$', login, name="login"),
    url(r'^login/efetuar_login$', efetuar_login, name="efetuar_login"),
    url(r'^login/sair$', sair, name="sair"),
    url(r'^cadastrar/$', cadastrar, name="cadastrar"),
    url(r'^cadastrar/efetuar_cadastro$', efetuar_cadastro, name="efetuar_cadastro"),
    url(r'^cadastrar/verifica_usuario_cadastrado$', verifica_usuario_cadastrado, name="verifica_usuario_cadastrado"),
    url(r'^home/$', home, name="home"),
    url(r'^produtos/$', produtos, name="produtos"),
    url(r'^produtos/cadastrar_produto$', cadastrar_produto, name="cadastrar_produto"),
    url(r'^produtos/dados_do_produto$', dados_do_produto, name="dados_do_produto"),
    url(r'^produtos/produto_cadastrado$', produto_cadastrado, name="produto_cadastrado"),
    url(r'^produtos/excluir_produto$', excluir_produto, name="excluir_produto"),
    url(r'^produtos/atualizar_produto$', atualizar_produto, name="atualizar_produto"),

]