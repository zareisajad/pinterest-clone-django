from unicodedata import name
from django.urls import path

from . import views

app_name = 'pinterest'

urlpatterns = [
    path('', views.home, name='home'),
    path('pin/<int:id>', views.pin_detail, name='pin_detail')
]