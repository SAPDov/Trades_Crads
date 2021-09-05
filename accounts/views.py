from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Profile, ProfileType
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import MyUserCreationForm, UserUpdateForm, ProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.views.generic import CreateView, DetailView
from cards.models import Card, Trade


# Create your views here.

def register(request):
	if request.method == 'POST':
		form = MyUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password1 = form.cleaned_data.get('password1')
			user = authenticate(username=username, password1=password1)
			if user:
				login(request, user)
				messages.success(request, f'Your account has been created! You are now able to log in')
			return redirect('login')
	else:
		form = MyUserCreationForm()
	return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileForm(request.POST,
								   request.FILES,
								   instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile')
  
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileForm(instance=request.user.profile)
  
	context = {
		'u_form': u_form,
		'p_form': p_form
	}
 
	return render(request, 'accounts/profile.html', context)


@login_required
def my_deck(request):
	card = Card.objects.all()
	trade = Trade.objects.all()
	return render(request, 'accounts/deck.html', {'trade': trade, 'card':card})

# class MyCard(DetailView):
# 	model = Card













