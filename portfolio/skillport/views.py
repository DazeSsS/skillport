from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Project
from .forms import CreateUserForm


class RegisterUser(CreateView):
    form_class = CreateUserForm
    template_name = 'skillport/sign_up.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'skillport/log_in.html'

    def get_success_url(self):
        return reverse_lazy('home')


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