from django.urls import path

from . import views

# class based component 
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns=[ 
    # changing function based to class based 
    # path('',views.home,name="blog-home"),
    path('',PostListView.as_view(),name="blog-home"),
    # this is to list all blogs of a specific user 
    path('user/<str:username>',UserPostListView.as_view(),name="user-posts"),
    # this is a post detail route
    path('post/<int:pk>',PostDetailView.as_view(),name="post-detail"),
    # this is a create post route 
    path('post/new/',PostCreateView.as_view(),name="post-create"),
    # this is a update blog route 
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name="post-update"),
    # this is to delete a blog post 
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name="post-delete"),
    

    path('about/',views.about,name="blog-about"),
]