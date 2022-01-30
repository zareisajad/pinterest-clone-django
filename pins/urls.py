from unicodedata import name
from django.urls import path

from . import views

app_name = 'pins'

urlpatterns = [
    path('create/', views.create_pin, name='create_pin'),
    path('edit/<int:id>', views.edit_pin, name='edit_pin'),
    path('delete/<int:id>', views.delete_pin, name='delete_pin'),
    path('comment/<int:id>', views.add_comment, name='add_comment'),
    path('delete-comment/<int:id>', views.delete_comment, name='delete_comment'),

    # path('/edit-comment/<int:id>', views.edit_comment, name='edit_comment'),


]