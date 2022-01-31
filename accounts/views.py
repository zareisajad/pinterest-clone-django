from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.contrib.auth.decorators import login_required

from boards.forms import CreateBoardForm
from .forms import UserRegistrationForm, UserLoginForm, EditProfileForm
from .models import User, Follow


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                data['email'], data['username'], data['password']
            )
            return redirect('accounts:user_login')
    else:
        form = UserRegistrationForm()
    context = {'title':'Signup', 'form':form}
    return render(request, 'register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('pinterest:home')
            else:
                messages.error(
                    request, 'username or password is wrong', 'danger'
                )
                return redirect('accounts:user_login')
    else:
        form = UserLoginForm()
    context = {'title':'Login', 'form': form}
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    return redirect('accounts:user_login')


@login_required
def follow(request, username):
    user = get_object_or_404(User, username=username)
    check_user = Follow.objects.filter(follower=request.user, following=user)
    if user == request.user:
        raise Http404
    elif check_user.exists():
        raise Http404
    else:
        follow = Follow.objects.create(follower=request.user, following=user)
        follow.save()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def unfollow(request, username):
    user = get_object_or_404(User, username=username)
    following = Follow.objects.filter(following=user).delete()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    boards = user.board_user.all()
    is_following = request.user.followers.filter(following=user).first()
    create_board_form = CreateBoardForm()
    context = {'user': user, 'boards':boards, 'is_following': is_following, 'create_board_form':create_board_form}
    return render(request, 'profile.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', request.user.username)
    else:
        form = EditProfileForm(instance=request.user.profile)
    context = {'title': 'Edit Profile', 'form': form}
    return render(request, 'edit_profile.html', context)