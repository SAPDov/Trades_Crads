import requests
import json
import django
import os



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cards_trade.settings')
django.setup()

from cards.models import Card



response = requests.get('https://rickandmortyapi.com/api/character').json()
data = response["results"]

print(data)

# for char in data:
# 	card = Card.objects.create(
# 		card_id= char['id'],
# 		name = char['name'],
# 		species= char['species'],
# 		origin = char['origin']['name'],
# 		img= char['image']
# 		)
# 	print(card)

