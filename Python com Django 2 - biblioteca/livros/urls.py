from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_filmes, name='listar_filmes'),
    path('<int:filme_id>/', views.detalhes_filme, name='detalhes_filme'),
    path('filme/adicionar/', views.adicionar_filme, name='adicionar_filme'),
    path('<int:filme_id>/editar/', views.editar_filme, name='editar_filme'),
    path('<int:filme_id>/excluir/', views.excluir_filme, name='excluir_filme'),
]
