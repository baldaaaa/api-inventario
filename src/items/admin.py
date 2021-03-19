from django.contrib import admin

from .models import Item, Etiqueta, Carpeta


admin.site.register(Item)
admin.site.register(Etiqueta)
admin.site.register(Carpeta)