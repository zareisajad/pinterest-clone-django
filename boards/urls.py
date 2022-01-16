from termios import VINTR
from unicodedata import name
from django.urls import path

from . import views

app_name = 'boards'

urlpatterns = [
    path('<str:board_name>/', views.create_board, name='create_board')
]