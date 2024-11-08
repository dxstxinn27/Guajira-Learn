from django.contrib import admin
from .models import Foro, Mensaje


class ForoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion')
    search_fields = ('titulo', 'descripcion')
    pass

admin.site.register(Foro, ForoAdmin)


class MensajeAdmin(admin.ModelAdmin):
    list_display = ('foro', 'autor', 'contenido', 'fecha_creacion')
    list_filter = ('fecha_creacion', 'autor_tipo')
    search_fields = ('contenido',)
    pass

admin.site.register(Mensaje, MensajeAdmin)


