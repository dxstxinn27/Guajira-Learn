from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from MyApps.usuarios.models import Estudiante, Docente, Tutor

class Foro(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.titulo} - {self.descripcion}"
    
    class Meta:
        verbose_name = "Foro"
        verbose_name_plural = "Foros"

class Mensaje(models.Model):
    foro = models.ForeignKey(Foro, on_delete=models.CASCADE, related_name="mensajes")
    autor_tipo = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model__in': ('estudiante', 'docente', 'tutor')})
    autor_id = models.PositiveIntegerField()
    autor = GenericForeignKey('autor_tipo', 'autor_id')
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def clean(self):
        
        if self.autor_tipo and self.autor_id:
            model_class = self.autor_tipo.model_class()
            if model_class not in [Estudiante, Docente, Tutor]:
                raise ValidationError("autor_tipo must be Estudiante, Docente, or Tutor.")

            try:
                
                model_class.objects.get(pk=self.autor_id)
            except model_class.DoesNotExist:
                raise ValidationError({
                    'autor_id': f"No {model_class.__name__} found with ID {self.autor_id}."
                })

    def __str__(self):
        return f"{self.autor} - {self.contenido[:20]}"
    
    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"
