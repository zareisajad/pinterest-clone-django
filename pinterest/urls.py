from unicodedata import name
from django.urls import path

from . import views

app_name = 'pinterest'

urlpatterns = [
    path('', views.home, name='home'),
    path('pin/<int:id>/', views.pin_detail, name='pin_detail'),
    path('<str:username>/_saved/', views.profile, name='profile'),
    path('settings/edit-profile/', views.edit_profile, name='edit_profile'),
    path('<str:username>/created/', views.created_pins, name='created_pins'),

]