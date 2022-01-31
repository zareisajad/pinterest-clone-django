from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import CreatePinForm, EditPinForm, CommentForm, SaveToBoard
from .models import Pin, Comment
from boards.models import Board
from accounts.forms import EditProfileForm
from accounts.models import User, Follow


@login_required
def create_pin(request):
    if request.method == 'POST':
        form = CreatePinForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            board = Board.objects.filter(id=instance.board.id).first()
            instance.save()
            board.pins.add(instance)
            return redirect('pins:pin_detail', instance.id)
    form = CreatePinForm(request.user)
    context = {'title': 'create pin', 'form': form} 
    return render(request, 'create_pin.html', context)


@login_required
def edit_pin(request, id):
    pin = get_object_or_404(Pin, id=id)
    if request.method == 'POST' and request.user == pin.user:
        form = EditPinForm(request.user, request.POST, instance=pin)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            board = Board.objects.filter(id=instance.board.id).first()
            instance.save()
            board.pins.add(instance)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def delete_pin(request, id):
    pin = get_object_or_404(Pin, id=id)
    if request.user == pin.user:
        pin.delete()
    return redirect('accounts:profile', request.user.username)


@login_required
def add_comment(request, id):
    pin = get_object_or_404(Pin, id=id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.pin = pin
            instance.user = request.user
            instance.save()
    return redirect(request.META.get('HTTP_REFERER'))


def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id).delete()
    return redirect(request.META.get('HTTP_REFERER'))


def get_related_pins(id):
    related_pins = []
    # get all boards
    boards = Board.objects.filter().all() 
    # get all boards that contains the current pin
    related_board = [
        board for board in boards if board.pins.filter(id=id).first()
    ] 
    # get all pins in related boards,
    # The output may be a nested list of queryset objects
    related_pins_lists = [board.pins.all() for board in related_board]
    # make ONE list of all pins
    for i in range(len(related_pins_lists)):
        for p in related_pins_lists[i]:
            related_pins.append(p)
    # remove current pin from related pins
    get_cuurent_pin = [
        related_pins.remove(pin) for pin in related_pins if pin.id == id
    ]
    return set(related_pins)


@login_required
def pin_detail(request, id):
    pin = Pin.objects.filter(id=id).first()
    saved_pin = request.user.pin_user.filter(id=id).first()
    is_following = request.user.followers.filter(following=pin.user).first()
    save_to_board_form = SaveToBoard(request.user, instance=saved_pin)
    edit_form = EditPinForm(request.user, instance=pin)
    comment_form = CommentForm()
    context = {
        'pin': pin,
        'save_to_board_form': save_to_board_form,
        'is_following': is_following,
        'edit_form': edit_form,
        'comment_form': comment_form,
        'related_pins': get_related_pins(id)
    }
    return render(request, 'pin_detail.html', context)


@login_required
def created_pins(request, username):
    user = get_object_or_404(User, username=username)
    created_pins = user.pin_user.all()
    is_following = request.user.followers.filter(following=user).first()
    context = {
        'created_pins': created_pins,
        'user': user,
        'is_following': is_following
    }
    return render(request, 'profile.html', context)
