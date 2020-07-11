from django.contrib import admin
from django.urls import path
from . import views

app_name = 'stories'

urlpatterns = [
    path('', views.all_stories, name='all_stories'),
    path('<int:content_id>/', views.content, name='stories'),
]
