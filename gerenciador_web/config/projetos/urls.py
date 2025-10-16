from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_projetos, name='lista_projetos'),#seria/projeto/
    path('<int:projeto_id>/', views.detalhe_projeto, name='detalhe_projeto'),
    #adicionar projeto
    path('adicionar/', views.adicionar_projeto,name = 'adicionar_projeto'),
    #adicionar projeto
    path('<int:projeto_id>/alterar/',views.alterar_projeto, name='alterar_projeto'),

    #excluir projeto 
    path ('<int:projeto_id>/excluir/', views.excluir_projeto ,name ='excluir_projeto')

    ]