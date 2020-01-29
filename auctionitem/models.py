from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import datetime
import pytz
print("Running for Mazzo")

class AuctionItem(models.Model):
	
	seller = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='auction_items')
	title = models.CharField(max_length=100)
	description = models.TextField()

	startBid = models.DecimalField(max_digits=6, decimal_places=2)
	buyNowPrice = models.DecimalField(max_digits=6, decimal_places=2)
	buyNowEnabled = models.BooleanField()
	deliveryCost = models.DecimalField(max_digits=6, decimal_places=2)
	
	now = datetime.datetime.now(tz=pytz.UTC)
	now_no_micro = now.replace(microsecond=0)
	now_stored = models.DateTimeField(default=now_no_micro)
	startDate = models.DateTimeField(default=now_no_micro)
	tdelta = datetime.timedelta(days=7)
	print(tdelta)
	enDate = now_no_micro + tdelta
	print(enDate)
	endDate =models.DateTimeField(default=enDate)
	print(endDate) 
	daysRemaining = 7
	viewCount=models.IntegerField(default=0)

	def __str__(self):
		return self.title

	# def save(self):
	# 	super().save()

	# 	img = Image.open(self.image.path)

	# 	if img.height > 300 or img.width > 300:
	# 		output_size = (300, 300)
	# 		img.thumbnail(output_size)
	# 		img.save(self.image.path)
	
	def getCurrentTopBid():
		return startBid

	def incrementViewCount(self):
		print('Hi Chris Mazzochi')
		self.viewCount = self.viewCount + 1
		self.save()

	def setDaysRemaining(self):
		eDate = self.endDate
		now   = self.now
		self.daysRemaining = eDate - now

		# daysRemaining = daysRemaining.strftime("%Y-%m-%d %H:%M:%S")

		self.save()
		print(self.daysRemaining)
		


	#def setDays(self):
	# 	self.days = self.startDate - self.endDate
	# 	self.save()

	# def setDaysRemaining(self):
	# 	self.daysRemaining = self.endDate - self.nowSaved
	# 	self.save()

	# def setDays(self, days):
	# 	if days != null: 
	# 		self.startDate = datetime.datetime.now()
	# 		self.endDate =   startDate + tdelta
	# 		self.days = endDate = startDate
