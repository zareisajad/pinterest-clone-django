from django.shortcuts import render, get_object_or_404

from pins.models import Pin
from accounts.models import User


def home(request):
    pins = Pin.objects.all()
    context = {'pins':pins[:49]}
    return render(request, 'home.html', context)


def pin_detail(request, id):
    pin = Pin.objects.filter(id=id).first()
    context = {'pin': pin}
    return render(request, 'pin_detail.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    pins = user.pin_user.all()
    boards = user.board_user.all()
    context = {'title': 'Profile', 'user': user, 'pins':pins, 'boards':boards}
    return render(request, 'profile.html', context)