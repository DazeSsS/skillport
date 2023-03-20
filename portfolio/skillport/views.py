from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# my views
from .forms import CreateUserForm


def register_page(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()

                user = form.cleaned_data.get('username')
                messages.success(request, 'Accout was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'skillport/register.html', context)


def login_page(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')
                return render(request, 'skillport/login.html')

        context = {}
        return render(request, 'skillport/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def index_page(request):
    return render(request, 'skillport/index.html')