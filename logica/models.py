from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    casado = models.BooleanField()
    def __str__(self):
        return self.nombre
    
class Tortuga(models.Model):
    nombre = models.CharField(max_length=50)
    velocidad = models.IntegerField()
    fuerza = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}_{self.id}"
    
class Pokemon(models.Model):
    nombre_pokemon = models.CharField(max_length=50)
    num_pokedex = models.IntegerField()
    tipo1 = models.CharField(max_length=50)
    tipo2 = models.CharField(max_length=50)
    hp = models.IntegerField()
    ataque = models.IntegerField()
    defensa = models.IntegerField()
    def __str__(self):
        return self.nombre_pokemon

class Chiste(models.Model):
    texto = models.CharField(max_length=255)
    def __str__(self):
        return self.texto


class Advice(models.Model):
    texto = models.CharField(max_length=255)
    def __str__(self):
        return self.texto


# === PLANTILLA: Nuevo modelo ===
# class NombreModelo(models.Model):
#     campo1 = models.CharField(max_length=255)
#     def __str__(self):
#         return self.campo1
#
# Luego: python manage.py makemigrations && python manage.py migrate