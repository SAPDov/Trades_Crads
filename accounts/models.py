from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProfileType(models.Model):
	name = models.CharField(max_length= 50)

	def __str__(self):
		return self.name
	def __repr__(self):
		return self.name


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	origin = models.ForeignKey(ProfileType, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='media/', null=True)


	def __str__(self):
		return self.user.username

	def __str__(self):
		return self.origin.name
