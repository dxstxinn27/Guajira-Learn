from django.contrib import admin
from .models import Estudiante, Docente, Tutor

# Register your models here.

class EstudianteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Estudiante, EstudianteAdmin)

class DocenteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Docente, DocenteAdmin)

class TutorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tutor, TutorAdmin)