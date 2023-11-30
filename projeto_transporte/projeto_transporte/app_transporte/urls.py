# app_transporte/urls.py
from django.urls import path
from .views import pagina_inicial
from .views import lista_funcionarios, cadastrar_funcionario, atualizar_funcionario, deletar_funcionario
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('lista_funcionarios/', views.lista_funcionarios, name='lista_funcionarios'),
    path('cadastrar_funcionario/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('atualizar_funcionario/<int:pk>/', views.atualizar_funcionario, name='atualizar_funcionario'),
    path('deletar_funcionario/<int:pk>/', views.deletar_funcionario, name='deletar_funcionario'),
]