from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserUpadteForm,ProfileUpadteForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# register view

def register(request):
     if request.method == 'POST':
          form = UserRegisterForm(request.POST) # Bind submitted form data to the form instance
          if form.is_valid():  # Check if the form data passes all validations
               form.save() # Save the user to the database
               username = form.cleaned_data.get('username') # Retrieve the username from the form
               messages.success(request , f'Your account has been created! You are now able to login {username}!')
               return redirect('login')
     else:
          form = UserRegisterForm() # Handles a GET request

     return render(request , 'users/register.html' , {'form' : form})


# profile view

@login_required # it adds functionality to our profile view that user must be logged in to view home pg 
def profile(request):
     if request.method == 'POST':
          u_form= UserUpadteForm(request.POST , instance=request.user) # we create instances for upadtion (it will automically add the feild to the user logged in)
          p_form=ProfileUpadteForm(request.POST , request.FILES , instance=request.user.profile)

          if u_form.is_valid() and p_form.is_valid():
               u_form.save()
               p_form.save()
               messages.success(request , f'Your details has been updated!')
               return redirect('profile')
    
     else:
          u_form= UserUpadteForm(instance=request.user)
          p_form=ProfileUpadteForm(instance=request.user.profile)

     context = {
          'u_form' : u_form,
          'p_form' : p_form
     }

     return render(request , 'users/profile.html' , context)


# The @login_required decorator ensures that only authenticated users can access the profile view.
#  If an unauthenticated user tries to access the view, they will be redirected to the login page. ...setting me b hm ne login url dia 
