from django.contrib import admin
from django.urls import path, include
from InstagApp.views import (
    Home, PostsView, PostDetailView, PostDeleteView, PostCreateView, PostUpdateView)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('posts/', PostsView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new', PostCreateView.as_view(), name='post_create'),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post_delete')
]
