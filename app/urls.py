from django.conf.urls import url

from app.views.views import *

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^login/$', login, name="login"),
    url(r'^login/efetuar_login$', efetuar_login, name="efetuar_login"),
    url(r'^login/sair$', sair, name="sair"),
    url(r'^cadastrar/$', cadastrar, name="cadastrar"),
    url(r'^cadastrar/efetuar_cadastro$', efetuar_cadastro, name="efetuar_cadastro"),
    url(r'^home/$', home, name="home"),
    url(r'^produtos/$', produtos, name="produtos"),

]