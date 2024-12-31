from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique = True)

    def __str__(self) -> str:
        return self.nombre

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self) -> str:
         return f"{self.titulo} ({self.categoria}) - {self.fecha}"
        