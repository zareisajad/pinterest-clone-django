from contextlib import redirect_stderr
from django.shortcuts import render, redirect

from .models import Board


def create_board(request, board_name):
    check_name = Board.objects.filter(title=board_name).first()
    if check_name == None:
        board = Board.objects.create(title=board_name, user=request.user)
    return redirect('pinterest:profile', request.user.username)