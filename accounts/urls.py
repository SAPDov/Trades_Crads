from django.urls import path, include
from . import views 

urlpatterns = [
	path('', include('django.contrib.auth.urls')),
   	path("register", views.register, name='register'),
   	# path("profile/<int:pk>", views.ProfileView.as_view(), name='profile'),
   	path("profile", views.profile, name='profile'),
   	path("profile/my_deck", views.my_deck, name='my_deck'),
    ]

