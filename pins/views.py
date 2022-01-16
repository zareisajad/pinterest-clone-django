from contextlib import redirect_stderr
from email import contentmanager
from multiprocessing import context
from django.shortcuts import render, redirect

from boards.models import Board

from .forms import CreatePinForm


def create_pin(requeset):
    if requeset.method == 'POST':
        form = CreatePinForm(requeset.POST, requeset.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = requeset.user
            board = Board.objects.filter(id=instance.board.id).first()
            instance.save()
            board.pins.add(instance)
            return redirect('pinterest:profile', requeset.user.username)

    else:
        form = CreatePinForm()
    context = {'title': 'create pin', 'form': form}
    return render(requeset, 'create_pin.html', context)