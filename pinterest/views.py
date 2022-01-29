from django.shortcuts import render, get_object_or_404, redirect

from pins.models import Pin
from pins.forms import SaveToBoard
from accounts.forms import EditProfileForm
from accounts.models import User
from boards.models import Board

def home(request):
    pins = Pin.objects.all()
    context = {'pins':pins[:49]}
    return render(request, 'home.html', context)


def pin_detail(request, id):
    pin = Pin.objects.filter(id=id).first()
    saved_pin = request.user.pin_user.filter(id=id).first()
    form = SaveToBoard(request.user, instance=saved_pin)
    if request.method == 'POST':
        form = SaveToBoard(request.user, request.POST, instance=saved_pin)
        board = Board.objects.filter(id=request.POST.get('board')).first()
        board.pins.add(pin)
        return redirect('pinterest:pin_detail', pin.id)
    context = {'pin': pin, 'form': form}
    return render(request, 'pin_detail.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    boards = user.board_user.all()
    context = {'title': 'Profile', 'user': user, 'boards':boards}
    return render(request, 'profile.html', context)


def created_pins(request,username):
    user = get_object_or_404(User, username=username)
    created_pins = user.pin_user.all()
    context = {'created_pins': created_pins}
    return render(request, 'profile.html', context)



def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('pinterest:profile', request.user.username)
    else:
        form = EditProfileForm(instance=request.user.profile)
    context = {'title': 'Edit Profile', 'form': form}
    return render(request, 'edit_profile.html', context)