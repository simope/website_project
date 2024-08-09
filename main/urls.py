from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('play/', views.play, name='play'),
    path('stats/', views.stats),
    path('play/save-to-DB/', views.save_to_DB, name='save_to_DB'),
    ]