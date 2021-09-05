from django.db import models
from accounts.models import Profile, ProfileType
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import random

# Create your models here.

class Card(models.Model):
	card_id = models.CharField(max_length=3, unique=True)
	name = models.CharField(max_length=30)
	species = models.CharField(max_length=30)
	origin = models.CharField(max_length=20)
	img = models.URLField()
	profiles = models.ManyToManyField(Profile, related_name='deck')


	def __str__(self):
		return self.name


#Checks if a user is created and then creates a profile to connect the two via the OneToOneField

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		origin = random.choice(ProfileType.objects.all())

		profile = Profile.objects.create(user=instance, origin=origin)
		instance.profile.save()

		profile.deck.add(*random.sample(list(Card.objects.all()), k=4))



# @receiver(post_save, sender=User) 
# def save_profile(sender, instance, **kwargs):
		


class Trade(models.Model):
	TRADE_STATUS = [
		('C','Close'),
		('O','Open'),
	]
	card = models.ForeignKey(Card, on_delete=models.CASCADE)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=1, choices=TRADE_STATUS)
	
	def __str__(self):
		return self.card.name


class Offer(models.Model):
	OFFER_STATUS = [
		('A','Accept'),
		('P','Pending'),
		('D', 'Decline'),
		]
	card = models.ForeignKey(Card, on_delete=models.CASCADE)
	profile = models.ForeignKey(Profile, models.CASCADE)
	trade = models.ForeignKey(Trade, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=1, choices=OFFER_STATUS, default='P')

	def __str__(self):
		return self.card.name

