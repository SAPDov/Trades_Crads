from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Profile, ProfileType


class MyUserCreationForm(UserCreationForm):
	username = forms.CharField(max_length=30, required=True)
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']


class ProfileForm(forms.ModelForm):
	image = forms.ImageField(required=False)
	origin = forms.CharField()

	class Meta:
		model = Profile
		fields = ['image', 'origin']

