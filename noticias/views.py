from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Noticia


# RASCUNHO DO BACK-END

def criar_noticias(request):
    if request.method == 'GET':
        return render(request, 'criarnot.html')

    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        subtitulo = request.POST.get('subtitulo')
        conteudo = request.POST.get('conteudo')
        autor = request.POST.get('autor')
        url_noticia = request.POST.get('url_noticia')
        data_noticia = request.POST.get('data_noticia')
        fonte = request.POST.get('fonte')
        categoria = request.POST.get('categoria')

        # Instanciando e salvando
        user = Noticia(titulo=titulo, subtitulo=subtitulo, conteudo=conteudo, autor=autor, url_noticia=url_noticia, data_noticia=data_noticia, fonte=fonte, categoria=categoria)
        user.save()

        return redirect('buscar_noticias')

def buscar_noticias(request):
    categoria = request.GET.get('categoria')

    if categoria:
        noticias = Noticia.objects.filter(categoria=categoria)
    else:
        noticias = Noticia.objects.all()

    return render(request, 'home.html', {'noticias': noticias})


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
    