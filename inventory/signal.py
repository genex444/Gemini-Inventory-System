# users/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Creates or updates a user profile when a new user is created or updated.
    """
    if created:
        # When a new user is created, create a corresponding UserProfile
        UserProfile.objects.create(user=instance)
    else:
        # If an existing user's data is updated, update the UserProfile
        instance.userprofile.save()
