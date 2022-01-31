from django.shortcuts import render, get_object_or_404, redirect

from pins.models import Pin
from pins.forms import SaveToBoard, EditPinForm, CommentForm
from accounts.forms import EditProfileForm
from accounts.models import User, Follow
from boards.models import Board


def home(request):
    pins = Pin.objects.all()
    context = {'pins':pins[:49]}
    return render(request, 'home.html', context)


def pin_detail(request, id):
    pin = Pin.objects.filter(id=id).first()
    is_following = request.user.followers.filter(following=pin.user).first()
    

    saved_pin = []
    for i in request.user.board_user.all():
        saved_pin.append(i.pins.filter(id=id).first())


    form = SaveToBoard(request.user, instance=saved_pin[-1])
    edit_form = EditPinForm(request.user, instance=pin)
    comment_form = CommentForm()

    if request.method == 'POST':
        form = SaveToBoard(request.user, request.POST, instance=saved_pin[-1])
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = pin.user
            instance.save()
            board = Board.objects.filter(id=request.POST.get('board')).first()
            board.pins.add(pin)
        return redirect(request.META.get('HTTP_REFERER'))


    context = {
        'pin': pin,
        'form': form,
        'is_following': is_following,
        'edit_form': edit_form,
        'comment_form': comment_form
    }
    return render(request, 'pin_detail.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    boards = user.board_user.all()
    is_following = request.user.followers.filter(following=user).first()
    context = {'user': user, 'boards':boards, 'is_following': is_following}
    return render(request, 'profile.html', context)


def created_pins(request, username):
    user = get_object_or_404(User, username=username)
    created_pins = user.pin_user.all()
    is_following = request.user.followers.filter(following=user).first()
    context = {
        'created_pins': created_pins,
        'user': user,
        'is_following': is_following
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if form.is_valid():
            form.save()
            return redirect('pinterest:profile', request.user.username)
    else:
        form = EditProfileForm(instance=request.user.profile)
    context = {'title': 'Edit Profile', 'form': form}
    return render(request, 'edit_profile.html', context)