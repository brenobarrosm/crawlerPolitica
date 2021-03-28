from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('/listaDeputados', views.listapoliticos, name='listaDosDeputados'),
    path('/presencaplenario', views.presencaplenario, name='presencaplenario'),
    path('/perfil/<int:id>', views.perfil, name='listardeputado'),
]
