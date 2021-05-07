from django.conf.urls import url

from app.views.views import *

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^login/$', login, name="login"),
    url(r'^cadastrar/$', cadastrar, name="cadastrar"),
]