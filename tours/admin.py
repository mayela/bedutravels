from django.contrib import admin
from .models import User, Zona, Tour

class TourAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "nombre", "slug", "operador", "tipoDeTour",
        "descripcion", "pais", "zonaSalida", "zonaLlegada")


# Register your models here.
admin.site.register(User)
admin.site.register(Zona)
admin.site.register(Tour, TourAdmin)