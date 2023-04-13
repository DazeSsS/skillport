from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm

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
        return render(request, 'skillport/sign_up.html', context)


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
                return render(request, 'skillport/log_in.html')

        context = {}
        return render(request, 'skillport/log_in.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def index_page(request):
    return render(request, 'skillport/index.html')


def feed_page(request):
    projects = Project.objects.all()
    context = {'projects': projects }
    return render(request, 'skillport/feed.html', context)


def project(request, pk):
    project = Project.objects.get(id = pk)
    tags =  project.tags.all()
    context = {'project': project, 'tags': tags}
    return render(request, 'skillport/single_project.html', context)


def create_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'skillport/project_form.html', context)