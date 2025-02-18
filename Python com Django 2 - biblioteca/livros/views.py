from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro
from .forms import LivroForm

def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, "livros/lista_livros.html", {"livros": livros})

def detalhes_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    return render(request, "livros/detalhes_livro.html", {"livro": livro})

def adicionar_livro(request):
    if request.method == "POST":
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_livros")
    else:
        form = LivroForm()
    return render(request, "livros/adicionar_livro.html", {"form": form})

def editar_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    if request.method == "POST":
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect("lista_livros")
    else:
        form = LivroForm(instance=livro)
    return render(request, "livros/editar_livro.html", {"form": form, "livro": livro})

def excluir_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    if request.method == "POST":
        livro.delete()
        return redirect("lista_livros")
    return render(request, "livros/excluir_livro.html", {"livro": livro})
