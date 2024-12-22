from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() # write unrestricted text lines....
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey( User, on_delete=models.CASCADE ) # if user is deleted the post is also deleted

    def __str__(self): # dunder __ method
        return self.title
    
    def get_absolute_url(self): # return url string
        return reverse("post-detail", kwargs={"pk": self.pk})
    

# reverse() is a built-in Django function that takes the name of a URL pattern and returns the actual URL string.