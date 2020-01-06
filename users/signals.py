#signal gets fired after an object has been saved.
from django.db.models.signals import post_save
#built in User model. It is the "sender"
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#decorator added to function, #A sender and a signal of post_save. 
#takes the signal-post_save, and the 
# sender which is the User. When a user is saved, send 
#the post_save signal it will be received by the receiver, 
#which is the create_profile and takes the arguments 
#the post_save signal sent to it. One of those is the 
#instance of the user, and the other is 'created', and saying
#if the User was created, then create a profile object with
#user equal to the instance of the user that was created.  

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created: 
		Profile.objects.create(user=instance)

#kwargs accepts any additional arguments that may have been
#added to the end of the function. 

#Save profile function that saves the profile
#every time the user object gets saved. 
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
	instance.profile.save()