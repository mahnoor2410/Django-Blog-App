from django.contrib import admin
from .models import Post # .model files me se Post class ko import kr rhy jo hm ne models.py me bnai he

# Register your models here.

admin.site.register(Post)