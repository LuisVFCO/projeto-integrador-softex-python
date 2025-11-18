from django.shortcuts import render
from django.http import HttpResponse
from .models import Noticia


# RASCUNHO DO BACK-END

# 1 - Listar noticias
def listar_noticias():
    # buscar notícias no banco.
    pass

# 2 -  Buscar por palavra
def filtrar_por_palavra(palavra):
    # filtrar notícias.
    pass

# 3 - Filtrar por município
def filtrar_por_municipio(municipio):
    # mostrar notícias do município específico.
    pass

# 4 - Filtrar por pauta
def filtrar_por_pauta(pauta):
    # separadas por categorias?
    pass

# 5 - Registrar acessos?
def registrar_acesso(noticia):
    # contador de acessos por clique?.
    pass

# 6 - Ranking
def ranking_noticias(limit=10):
    # Retorna as notícias com maior número de acessos.
    pass

# 7. Classificação por palavras-chave
def classificar(titulo, conteudo):
    # identificar pauta com base em palavras.
    pass

def ver_buscador_noticias(request):
    if request.method == "GET":
        nome = 'Luis'
        return render(request, 'ver_buscador.html', {'nome': 'nome'})
    elif request.method == "POST":
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        
        noticia = Noticia(titulo=titulo, descricao=descricao)

        noticia.save()
        
        return HttpResponse('dados cadastrados')