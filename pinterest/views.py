from django.shortcuts import render, get_object_or_404, redirect

from pins.models import Pin
from accounts.forms import EditProfileForm
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