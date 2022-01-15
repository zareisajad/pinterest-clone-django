from multiprocessing import context
from django.shortcuts import render, redirect

from boards.models import Board
from pins.models import Pin


def home(request):
    pins = Pin.objects.all()
    context = {'pins':pins}
    return render(request, 'home.html', context)
