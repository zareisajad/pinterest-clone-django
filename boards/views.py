from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Board


@login_required
def create_board(request, board_name):
    check_name = request.user.board_user.filter(title=board_name).first()
    if not check_name:
        board = Board.objects.create(title=board_name, user=request.user)
    return redirect('accounts:profile', request.user.username)


@login_required
def board_detail(request, username, board_name):
    board = get_object_or_404(Board, title=board_name)
    pins = board.pins.all()
    context = {'pins': pins}
    return render(request, 'board_detail.html', context)


@login_required
def edit_board(request, id):
    board = get_object_or_404(Board, id=id)
    return redirect(request.META.get('HTTP_REFERER'))

