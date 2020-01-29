from django.urls import path
from .views import (
	AuctionItemListView, 
	AuctionItemDetailView,
	AuctionItemCreateView,
	AuctionItemUpdateView,
	AuctionItemDeleteView,
    UserAuctionItemListView
	)
from . import views

urlpatterns = [
    path('list/', AuctionItemListView.as_view(), name='auctionitem-list'),
    path('user/<str:username>', UserAuctionItemListView.as_view(), name='user-auctionitems'),
    path('auctionitem/<int:pk>/', AuctionItemDetailView.as_view(), name='auctionitem-detail'),
    path('new/', AuctionItemCreateView.as_view(), name='auctionitem-create'),
    path('auctionitem/<int:pk>/update', AuctionItemUpdateView.as_view(), name='auctionitem-update'), 
    path('auctionitem/<int:pk>/delete', AuctionItemDeleteView.as_view(), name='auctionitem-delete'),  
]
