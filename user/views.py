from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from user.forms.profile_form import ProfileForm
from user.models import Profile
from django.contrib.auth import (authenticate, login)


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    next = request.GET.get('next')
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'user/register.html', context)

def edit_profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/edit_profile.html', {
        'form': ProfileForm(instance=profile)
    })

def profile(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, '../templates/user/profile.html')