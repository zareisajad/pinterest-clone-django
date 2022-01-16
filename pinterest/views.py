from multiprocessing import context
from django.shortcuts import render, redirect

from boards.models import Board
from pins.models import Pin


def home(request):
    pins = Pin.objects.all()
    context = {'pins':pins[:49]}
    return render(request, 'home.html', context)


def pin_detail(request, id):
    pin = Pin.objects.filter(id=id).first()
    context = {'pin': pin}
    return render(request, 'pin_detail.html', context)

