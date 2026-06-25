import os
import sys
import django

# Agregar la raíz del proyecto al path para que encuentre 'backend' y 'logica'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

import requests
from logica.models import Chiste
cantidad = 100
for i in range(cantidad):
    response = requests.get('https://api.chucknorris.io/jokes/random')
    data = response.json()

    chiste_texto = data['value']
    Chiste.objects.create(texto=chiste_texto)

    print("Chiste guardado:", chiste_texto)