from django.urls import path

from . import views

app_name = 'boards'

urlpatterns = [
    path('create/', views.create_board, name='create_board'),
    path('<str:username>/<str:board_name>/', views.board_detail, name='board_detail'),
    path('<int:id>/', views.edit_board, name='edit_board'),
    path('save/<int:id>', views.save_to_board, name='save_to_board'),
    path('remove/<int:pin_id>/<int:board_id>/', views.remove_from_board, name='remove_from_board'),
]