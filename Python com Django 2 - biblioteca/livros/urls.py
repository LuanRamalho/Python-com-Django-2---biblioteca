from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_livros, name="lista_livros"),
    path("livro/<int:livro_id>/", views.detalhes_livro, name="detalhes_livro"),
    path("adicionar/", views.adicionar_livro, name="adicionar_livro"),
    path("editar/<int:livro_id>/", views.editar_livro, name="editar_livro"),
    path("excluir/<int:livro_id>/", views.excluir_livro, name="excluir_livro"),
]
