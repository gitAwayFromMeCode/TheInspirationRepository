from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#we need a profile to be created when a user is created, hence the sender will be User
#when the user is saved the Profile will be saved also
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()