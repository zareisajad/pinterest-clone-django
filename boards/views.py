from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Board


@login_required
def create_board(request, board_name):
    check_name = request.user.board_user.filter(title=board_name).first()
    if check_name == None:
        board = Board.objects.create(title=board_name, user=request.user)
    return redirect('accounts:profile', request.user.username)


@login_required
def board_detail(request,username, board_name):
    board = Board.objects.filter(title=board_name).first()
    pins = board.pins.all()
    context = {'pins': pins}
    return render(request, 'board_detail.html', context)