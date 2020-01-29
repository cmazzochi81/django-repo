from django import forms
from django.contrib.auth.models import AuctionItem
from django.contrib.auth.forms import AuctionItemCreationForm
#from .models import Profile

class AuctionItemRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta: 
		model = User
		fields = ['username', 'email', 'password1', 'password2']