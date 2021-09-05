from django.urls import path
from . import views 

urlpatterns = [
     path("all_cards/",  views.CardsListView.as_view(), name='all_cards'),
    ]