from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tweets/', views.tweet_list, name='tweet_list'),
    path('tweets/create/', views.create_tweet, name='create_tweet'),
    path('tweets/<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('tweets/<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    path('register/', views.register, name='register'),
]