from django import forms
from django.contrib.auth.models import User # built-in model he yh overall 
from django.contrib.auth.forms import UserCreationForm  # built-in form he handle user registration
from .models import Profile  # to update profile pic

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # Customizing Field we can also add more

    class Meta: # provide metadata about the form, such as which model the form is based on and which fields to include or exclude
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2'] # Default Fields

# the class we make in in is imported in views.py file we can also use UserCreationForm but for customization we make a separate file
 

class UserUpadteForm(forms.ModelForm):  # to update username,email 
    email = forms.EmailField()

    class Meta: 
        model = User
        fields = ['username' , 'email'] 

class ProfileUpadteForm(forms.ModelForm):  # to update profile pic
    class Meta: 
        model = Profile
        fields = ['image']