from unicodedata import name
from django.urls import path

from . import views

app_name = 'pins'

urlpatterns = [
    path('create/', views.create_pin, name='create_pin'),
    path('edit/<int:id>', views.edit_pin, name='edit_pin'),
    path('delete/<int:id>', views.delete_pin, name='delete_pin'),

]