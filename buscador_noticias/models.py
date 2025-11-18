from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self) -> str:
        return self.titulo
