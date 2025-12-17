from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    autor = models.CharField(max_length=100)
    url_noticia = models.URLField(max_length=300)
    data_noticia = models.DateField()
    fonte = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.titulo} - {self.categoria}"
