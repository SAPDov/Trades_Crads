from django.shortcuts import render
from .models import Card, Trade
from django.views.generic import ListView

# Create your views here.

class CardsListView(ListView):
	model = Card
	template_name = 'cards/cards_list.html'



# def add_card_to_deck(request, card_id):
# 	if request.method == 'POST':
# 		Card.objects.create()

# class TradesListView(ListView):
# 	model = Trade
# 	template_name = 'cards/trads_list.html'
# 	ordering = '-date'



def tradesView(request):
    trades = Trade.objects.filter(status='P').order_by('-date')
    return render(request, 'cards/tradesView.html', {'trades': trades})



