from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

# to get the data from database 
from .models import Post

# import user module 
from django.contrib.auth.models import User

# to check the user who is updating and add post only when loggedin 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# to show list view 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



# Create your views here.

# posts=[ 
#     {
#         'author':'CoreyMS',
#         'title':'Blog Post1',
#         'content':'First post content',
#         'date_posted':'August 27,2018'
#     },
#     {
#         'author':'Jane Doe',
#         'title':'Blog Post2',
#         'content':'Second post content',
#         'date_posted':'August 28,2018'
#     }
# ]


# this is a function method for home
def home(request):
    context={
        # 'posts':posts
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)


# this is class method for home 
class PostListView(ListView):
    model=Post
    template_name='blog/home.html'
    context_object_name='posts'
    ordering= ['-date_posted']
    
    # for pagination 
    paginate_by = 5

# to list posts by specific user 
class UserPostListView(ListView):
    model=Post
    template_name='blog/user_posts.html'
    context_object_name='posts'
    
    
    # for pagination 
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model=Post
    


class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']

    def form_valid(self, form):
        form.instance.author= self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']

    def form_valid(self, form):
        form.instance.author= self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post=self.get_object()
        if self.request.user== post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model=Post
    success_url= '/'
    def test_func(self):
        post=self.get_object()
        if self.request.user== post.author:
            return True
        return False


def about(request):
    return render(request,'blog/about.html',{
        'title':'About..'
    })