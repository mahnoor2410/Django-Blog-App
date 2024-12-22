from django.shortcuts import render , get_object_or_404
from .models import Post # .model files me se Post class ko import kr rhy jo hm ne models.py me bnai he
from django.views.generic import (
    ListView , 
    DetailView , 
    CreateView ,
    UpdateView ,
    DeleteView
) 
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.auth.models import User

# Create your views here

def home(request):
    context = {
        'posts' : Post.objects.all()  # Query to get all Post objects from the database
    }
    return render(request,"blog/home.html" , context)

# ================================ HOME PAGE VIEW ============================

class PostListView(ListView): # class based view
    model = Post  # ListView will automatically query the "Post model" for all post objects(hr aik post).
    template_name ='blog/home.html'  # <app>/<model>_<viewtype>.html    
    context_object_name = 'posts' # Renames the default context (object_list) to posts--- mtlb hm yh wali key use kry gy home page pe varibale ko access krny k lea 
    ordering = ['-date_posted'] # latest post phly show kry ga yh
    paginate_by = 4

class UserPostListView(ListView): # sem upr wali class he 
    model = Post  
    template_name ='blog/user_posts.html'   
    context_object_name = 'posts' 
    paginate_by = 4

    def get_queryset(self): # Retrieves the value of the username parameter passed in the URL
        user = get_object_or_404(User , username=self.kwargs.get('username')) # the query parameters 
        return Post.objects.filter(author=user).order_by('-date_posted') # Filters the Post model to include only the posts authored by the User object (user) obtained in the previous step.

# ================================ DETAILED PAGE (Displays details of a single post) ============================

class PostDetailView(DetailView): 
    model = Post # This specifies that we are using the 'Post' model from models.py
    # template_name = 'blog/post_detail.html'  # This line is ""optional"" as it is the default
    # context_object_name = 'object'  # Default context object name is 'object'

# ================================ CREATE PAGE VIEW ============================

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title' , 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user # we r giving author here for post which is creating
        return super().form_valid(form)

# ================================ UPDATE PAGE VIEW ============================

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title' , 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user # we r giving author here for post which is creating
        return super().form_valid(form)
    
    def test_func(self): # yh function dusro ki post update ni krny de ga
        post = self.get_object()
        if self.request.user == post.author: # also make sure that the post has the author of current loggedIn user
            return True
        return False

# ================================ DELETE PAGE VIEW WITH POST IDS WE CAN ACCESS SIGNLE POST ============================

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' # It will delete post after we give this url and Redirects users to the home page after deletion.
    
    def test_func(self): # yh function dusro ki post update ni krny de ga
       post = self.get_object()
       if self.request.user == post.author:
            return True
       return False

def about(request):
    return render(request,"blog/about.html" , {'title' : 'About'}) # it shows title with Django Blog - ()



# LoginRequiredMixin: Ensures the user is logged in before accessing the view.
# UserPassesTestMixin: Adds a custom test (e.g., is the user the author of the post?) to further restrict access.
