from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('selecao/', views.selecao_view, name='selecao'),
    path('interface-a/', views.interface_a_view, name='interface_a'),
    path('interface-b/', views.interface_b_view, name='interface_b'),
    path('clientes/criar/', views.criar_cliente_view, name='criar_cliente'),
    path('clientes/excluir/<int:pk>/', views.excluir_cliente_view, name='excluir_cliente'),
    path('survey/', views.survey_view, name='survey'),
]
