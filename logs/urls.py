"""Defines URL patterns for the logs"""

from django.urls import path
from . import views

app_name = 'logs'
urlpatterns = [
    #Home page

    path('logs/', views.logs, name="logs"),


]
