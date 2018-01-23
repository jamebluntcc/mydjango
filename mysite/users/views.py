from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, forms
# Create your views here.


def user_login(request):
    if request.POST:
        username = request.POST.get('username')
        passwd = request.POST.get('password')
        user = authenticate(username=username, password=passwd)
        if user and user.is_active:
            login(request, user)
            return redirect('/')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('/')


def user_register(request):
    if request.POST:
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect('/')
    form = forms.UserCreationForm()
    return render(request, 'register.html', context={'form': form})


