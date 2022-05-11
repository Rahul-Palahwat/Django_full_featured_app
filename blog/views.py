from django.shortcuts import render

from django.http import HttpResponse

# to get the data from database 
from .models import Post

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


def home(request):
    context={
        # 'posts':posts
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{
        'title':'About..'
    })