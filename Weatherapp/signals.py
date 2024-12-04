# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User

# This function runs after a user is saved, and it creates a corresponding Profile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)  # Create Profile for the new user

# This function runs after a user is saved, and it updates the corresponding Profile if the user details are updated
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()  # Save the profile after the user is updated
