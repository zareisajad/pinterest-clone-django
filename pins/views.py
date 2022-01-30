from django.shortcuts import render, redirect

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
    pin = Pin.objects.filter(id=id).first()
    if request.method == 'POST':
        form = EditPinForm(request.user, request.POST, instance=pin)
        if form.is_valid():
            form.save()
    return redirect(request.META.get('HTTP_REFERER'))

