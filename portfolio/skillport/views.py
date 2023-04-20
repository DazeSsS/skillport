from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from .models import Project
from .forms import CreateUserForm, CreateProjectForm


class RegisterUser(CreateView):
    form_class = CreateUserForm
    template_name = 'skillport/sign_up.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'skillport/log_in.html'

    def get_success_url(self):
        return reverse_lazy('home')


class CreateProject(LoginRequiredMixin, CreateView):
    form_class = CreateProjectForm
    template_name = 'skillport/create.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        form.save()
        return redirect('profile')


def logout_user(request):
    logout(request)
    return redirect('home')


def index_page(request):
    projects = Project.objects.order_by('-date')
    return render(request, 'skillport/index.html', {'projects': projects})


def profile_page(request):
    user_projects = request.user.projects.order_by('-date')
    return render(request, 'skillport/profile.html', {'user_projects': user_projects})


def favorites_page(request):
    favorites = request.user.likes.order_by('-date')
    return render(request, 'skillport/favorites.html', {'favorites': favorites})


def set_like(request):
    project = get_object_or_404(Project, id=request.POST.get('project_id'))
    if request.user not in project.likes.all():
        project.likes.add(request.user)
    else:
        project.likes.remove(request.user)
    return HttpResponseRedirect(reverse('home'))

# def feed_page(request):
#     projects = Project.objects.all()
#     context = {'projects': projects }
#     return render(request, 'skillport/feed.html', context)


# def project(request, pk):
#     project = Project.objects.get(id = pk)
#     tags =  project.tags.all()
#     context = {'project': project, 'tags': tags}
#     return render(request, 'skillport/single_project.html', context)


# def create_project(request):
#     form = ProjectForm()
#     if request.method == 'POST':
#         form = ProjectForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('projects')
#     context = {'form': form}
#     return render(request, 'skillport/project_form.html', context)