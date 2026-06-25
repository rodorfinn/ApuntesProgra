import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

import requests
from logica.models import NombreModelo

URL = "https://api.ejemplo.com/endpoint"
cantidad = 100

for i in range(cantidad):
    response = requests.get(URL)
    data = response.json()
    valor = data['campo_que_quiero']
    NombreModelo.objects.create(campo1=valor)
    print(f"{i+1}. Guardado: {valor}")

print(f"¡Listo! Se guardaron {cantidad} registros.")