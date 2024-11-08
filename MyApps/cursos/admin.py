from django.contrib import admin
from .models import Asignatura, Tema

# Register your models here.

class AsignaturaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Asignatura, AsignaturaAdmin)

class TemaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tema, TemaAdmin)