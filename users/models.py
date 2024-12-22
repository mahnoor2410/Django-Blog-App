# The Profile model is designed to store additional information about a user 
# that is not included in the default User model provided by Django

from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    # Fields in the Profile Model
    user = models.OneToOneField(User,on_delete=models.CASCADE) # user del ... profile pic also del 
    image = models.ImageField(default='defaultpic.jpg',upload_to='profile_pics')
     

    def __str__(self):
        return f'{self.user.username} Profile'
    
# (OneToOneField) links the Profile model to Django’s built-in User model
# (__str__) defines the string representation


# we do changings here which also save profile pic
    def save(self, *args, **kwargs):  # Ensure compatibility with Django's ORM
        super().save(*args, **kwargs)  # Call the parent class's save method

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    

# Added *args and **kwargs to save():
#     This ensures that any arguments passed by Django (such as force_insert or force_update) are forwarded correctly to the parent save() method.
#     Without this, Django raises the TypeError.