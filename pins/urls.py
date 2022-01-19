from unicodedata import name
from django.urls import path

from . import views

app_name = 'pins'

urlpatterns = [
    path('create/', views.create_pin, name='create_pin'),
]