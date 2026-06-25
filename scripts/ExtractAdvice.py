import os
import sys
import django

# Agregar la raíz del proyecto al path para que encuentre 'backend' y 'logica'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

import requests
from logica.models import Advice
cantidad = 100
for i in range(cantidad):
    response = requests.get('https://api.adviceslip.com/advice')
    data = response.json()

    advice_text = data['slip']
    Advice.objects.create(texto=advice_text)

    print("Consejo guardado:", advice_text)