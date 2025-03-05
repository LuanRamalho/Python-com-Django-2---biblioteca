from django.shortcuts import render, redirect, get_object_or_404
from .models import Filme
from .forms import FilmeForm

def listar_filmes(request):
    query = request.GET.get('q')
    if query:
        filmes = Filme.objects.filter(titulo__icontains=query)
    else:
        filmes = Filme.objects.all()
    return render(request, 'filmes/listar.html', {'filmes': filmes})

def adicionar_filme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_filmes')
    else:
        form = FilmeForm()
    return render(request, 'filmes/adicionar_filme.html', {'form': form})


def detalhes_filme(request, filme_id):
    filme = get_object_or_404(Filme, pk=filme_id)
    return render(request, 'filmes/detalhes.html', {'filme': filme})

def editar_filme(request, filme_id):
    filme = get_object_or_404(Filme, pk=filme_id)
    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES, instance=filme)
        if form.is_valid():
            form.save()
            return redirect('detalhes_filme', filme_id=filme.id)
    else:
        form = FilmeForm(instance=filme)
    return render(request, 'filmes/editar.html', {'form': form, 'filme': filme})


def excluir_filme(request, filme_id):
    filme = get_object_or_404(Filme, pk=filme_id)
    if request.method == 'POST':
        filme.delete()
        return redirect('listar_filmes')
    return render(request, 'filmes/excluir.html', {'filme': filme})
