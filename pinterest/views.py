from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from pins.models import Pin


@login_required
def home(request):
    pins = Pin.objects.all()
    context = {'pins':pins[:49]}
    return render(request, 'home.html', context)
