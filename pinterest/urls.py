from unicodedata import name
from django.urls import path

from . import views

app_name = 'pinterest'

urlpatterns = [
    path('', views.home, name='home')
]