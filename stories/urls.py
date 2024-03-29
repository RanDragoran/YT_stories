from django.contrib import admin
from django.urls import path
from . import views

app_name = 'stories'

urlpatterns = [
    path('all/<int:content_id>/', views.content, name='stories'),
    path('one/<int:story_id>/', views.one_story, name='one_story'),
    path('archive/', views.archive, name='archive'),
]
