from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Asignatura(models.Model):
    nombre = models.CharField(max_length=30, help_text="Nombre de la asignatura")
    descripcion = models.TextField(max_length=250, help_text="Descripción de la asignatura")
    creditos = models.IntegerField(help_text="Créditos de la asignatura", validators=[MinValueValidator(1), MaxValueValidator(4)])
    codigo = models.IntegerField(help_text="Código de la asignatura")

    def __str__(self):
        return f'{self.nombre} -> {self.codigo}'
    
    class Meta:
        verbose_name = "asignatura"
        verbose_name_plural = "asignaturas"

class Tema(models.Model):
    titulo = models.CharField(max_length=30, help_text="Título del tema")
    descripcion = models.TextField(max_length=250, help_text="Descripción del tema")
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, help_text="Asignatura del tema")
    #recor = models.FileField(help_text="Prueba")

    def __str__(self):
        return f'{self.titulo} -> {self.asignatura}'
    
    class Meta:
        verbose_name = "tema"
        verbose_name_plural = "temas"