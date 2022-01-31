from django.shortcuts import render, redirect, get_object_or_404

from boards.models import Board
from .forms import CreatePinForm, EditPinForm, CommentForm
from .models import Pin, Comment


def create_pin(request):
    if request.method == 'POST':
        form = CreatePinForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            board = Board.objects.filter(id=instance.board.id).first()
            instance.save()
            board.pins.add(instance)
            return redirect('pinterest:pin_detail', instance.id)
    form = CreatePinForm(request.user)
    context = {'title': 'create pin', 'form': form} 
    return render(request, 'create_pin.html', context)


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


def delete_pin(request, id):
    pin = get_object_or_404(Pin, id=id)
    if request.user == pin.user:
        pin.delete()
    return redirect('pinterest:profile', request.user.username)


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



# def edit_comment(request, id):
#     comment = get_object_or_404(Comment, id=id)
#     if request.method == 'POST':
#         form = CommentForm(request.POST, instance=comment)
#         if form.is_valid():
#             form.save()
#     return redirect(request.META.get('HTTP_REFERER'))
