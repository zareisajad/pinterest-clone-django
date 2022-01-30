from django.shortcuts import render, redirect, get_object_or_404

from boards.models import Board
from .forms import CreatePinForm, EditPinForm
from .models import Pin


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
            form.save()
    return redirect(request.META.get('HTTP_REFERER'))


def delete_pin(request, id):
    pin = get_object_or_404(Pin, id=id).delete()
    return redirect('pinterest:profile', request.user.username)
