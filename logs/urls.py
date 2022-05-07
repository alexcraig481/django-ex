"""Defines URL patterns for the logs"""

from django.urls import path
from . import views

app_name = 'logs'
urlpatterns = [
    #Home page

    path('logs/', views.logs, name="logs"),
    path('logs/<int:log_id>/', views.log_entry, name='log_entry'),
    path('new_entry/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:log_id>/', views.edit_entry, name='edit_entry')


]
