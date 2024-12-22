# Django's signals allow you to attach custom behavior to certain actions, like creating or saving a model instance.

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# we want user profile pic will be craeted for each user

@receiver(post_save,sender=User)
def create_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance, **kwargs): # accepts additional keyword arg
    instance.profile.save()


# post_save: This signal is sent after a model's save() method is called.
# @receiver decorator: Used to connect a function (signal handler) to a specific signal.
# signal handlers : create_profile , save_profile