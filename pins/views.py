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
    if request.method == 'POST':
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


@login_required
def pin_detail(request, id):
    pin = Pin.objects.filter(id=id).first()
    is_following = request.user.followers.filter(following=pin.user).first()
    saved_pin = request.user.pin_user.filter(id=id).first()
    form = SaveToBoard(request.user, instance=saved_pin)
    edit_form = EditPinForm(request.user, instance=pin)
    comment_form = CommentForm()
    if request.method == 'POST':
        form = SaveToBoard(request.user, request.POST, instance=saved_pin)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = pin.user
            instance.save()
            board = Board.objects.filter(id=request.POST.get('board')).first()
            board.pins.add(pin)
        return redirect(request.META.get('HTTP_REFERER'))
    context = {
        'pin': pin,
        'form': form,
        'is_following': is_following,
        'edit_form': edit_form,
        'comment_form': comment_form
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
