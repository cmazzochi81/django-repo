from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import (
	LoginRequiredMixin, 
	UserPassesTestMixin
)
from django.contrib.auth.models import User
from django.views.generic import (
		ListView, 
		DetailView, 
		CreateView,
		UpdateView,
		DeleteView
		)

from .models import AuctionItem

class AuctionItemListView(ListView):
	model = AuctionItem               #looks dir of app name   #template  #view
	template_name = 'auctionitem/auctionitem_list.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'auctionitems'
	ordering = ['-startDate']
	paginate_by = 2

class UserAuctionItemListView(ListView):
	model = AuctionItem                #looks dir of app name   #template  #view
	template_name = 'auctionitem/user_auctionitems.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'auctionitems'
	ordering = ['-date_posted']
	paginate_by = 2

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return AuctionItem.objects.filter(seller=user).order_by('-startDate')

class AuctionItemDetailView(DetailView):
	model = AuctionItem
		
class AuctionItemCreateView(LoginRequiredMixin, CreateView):
	model = AuctionItem
	fields = ['image', 'title', 'description', 'startBid', 'buyNowPrice', 'buyNowEnabled', 'startDate', 'endDate', 'deliveryCost', 'seller']
	success_url ='/'
	def form_valid(self,form):
		form.instance.seller = self.request.user
		return super().form_valid(form)

class AuctionItemUpdateView(LoginRequiredMixin,UpdateView):
	model = AuctionItem
	fields = ['title', 'description', 'startBid', 'buyNowPrice', 'buyNowEnabled', 'startDate', 'deliveryCost', 'seller']
	success_url ='/'

	def form_valid(self,form):
		form.instance.seller = self.request.user
		return super().form_valid(form)

		def test_func(self):
			post = self.get_object()
			if self.request.user == auctionitem.seller:
				return True
			return False

class AuctionItemDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
	model = AuctionItem
	success_url ='/'

	def test_func(self):
		auctionitem = self.get_object()
		if self.request.user == auctionitem.seller:
			return True
		return False