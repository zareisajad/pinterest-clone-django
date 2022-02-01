from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from pins.models import Pin
from pins.forms import SaveToBoard
from .models import Board
from .forms import CreateBoardForm, EditBoardForm


@login_required
def create_board(request):
    if request.method == 'POST':
        form = CreateBoardForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            check_name = request.user.board_user.filter(
                title=instance.title
            ).first()
            if not check_name:
                instance.save()
    return redirect('accounts:profile', request.user.username)


@login_required
def board_detail(request, username, board_name):
    board = get_object_or_404(Board, title=board_name)
    pins = board.pins.all()
    context = {'pins': pins, 'board': board}
    return render(request, 'board_detail.html', context)


@login_required
def edit_board(request, id):
    board = request.user.board_user.filter(id=id).first()
    if request.method == 'POST':
        form = EditBoardForm(request.POST, request.FILES, instance=board)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', request.user.username)
    form = EditBoardForm(instance=board)
    context = {'board': board ,'form': form}
    return render(request, 'edit_board.html', context)


@login_required
def save_to_board(request, id):
    pin = Pin.objects.filter(id=id).first()
    saved_pin = request.user.pin_user.filter(id=id).first()
    if request.method == 'POST':
        form = SaveToBoard(request.user, request.POST, instance=saved_pin)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = pin.user
            instance.save()
            board = Board.objects.filter(id=request.POST.get('board')).first()
            board.pins.add(pin)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_board(request, pin_id, board_id):
    board = request.user.board_user.filter(id=board_id).first()
    get_pin = board.pins.filter(id=pin_id).first()
    if get_pin:
        board.pins.remove(get_pin)
    return redirect(request.META.get('HTTP_REFERER'))
