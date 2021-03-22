from django.urls import path
from . import views

urlpatterns = [
    path('', views.paginaInicial, name ='index'),
    path('paginaGrupo', views.paginaGrupo, name='paginaGrupo'),
    path('login', views.login, name='login')
]