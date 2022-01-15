from multiprocessing import context
from django.shortcuts import render, redirect


def home(request):
    context = {}
    return render(request, 'home.html', context)
