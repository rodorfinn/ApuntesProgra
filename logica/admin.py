from django.contrib import admin
from logica.models import Persona, Tortuga, Pokemon, Chiste, Advice

# Register your models here.

admin.site.register(Persona)
admin.site.register(Tortuga)
admin.site.register(Pokemon)
admin.site.register(Chiste)
admin.site.register(Advice)

# === PLANTILLA: Registrar modelo ===
# from .models import NombreModelo
# admin.site.register(NombreModelo)