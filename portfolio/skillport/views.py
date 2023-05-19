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
from .forms import CreateCommentForm
from .models import Comment

from .models import Project, Person
from .forms import CreateUserForm, CreatePersonForm, CreateProjectForm


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'skillport/log_in.html'

    def get_success_url(self):
        return reverse_lazy('home')


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        person_form = CreatePersonForm(request.POST)

        if form.is_valid() and person_form.is_valid():
            user = form.save()

            person = person_form.save(commit=False)
            person.user = user

            person.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('home')
    else:
        form = CreateUserForm()
        person_form = CreatePersonForm()

    context = { 'form': form, 'person_form': person_form }
    return render(request, 'skillport/sign_up.html', context)


class CreateProject(LoginRequiredMixin, CreateView):
    form_class = CreateProjectForm
    template_name = 'skillport/create.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user.person
        form.save()
        return redirect('profile')


def logout_user(request):
    logout(request)
    return redirect('home')


def index_page(request):
    projects = Project.objects.order_by('-date')
    return render(request, 'skillport/index.html', {'projects': projects})


def profile_page(request):
    user_projects = request.user.person.projects.order_by('-date')
    return render(request, 'skillport/profile.html', {'user_projects': user_projects})


def another_profile_page(request, user_id):
    user = get_object_or_404(Person, pk=user_id)
    user_projects = Project.objects.filter(author=user).order_by('-date')
    subscribed = True if user in request.user.person.subscriptions.all() else False
    return render(request, 'skillport/another_profile.html', {'user': user, 'user_projects': user_projects, 'subscribed': subscribed})


def project_page(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    comments = Comment.objects.filter(project = project)
    
    form = CreateCommentForm()
    if request.method == "POST": 
        if request.user.is_authenticated:
            form = CreateCommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user.person
                comment.project = project
                comment.save()
                form = CreateCommentForm()
                return redirect('project', project_id)
        else:
            messages.error(request, "Необходимо войти в аккаунт, чтобы оставлять комментарии")

    another = project.author.projects.exclude(id=project_id).order_by('-date')[:3]
    subscribed = True if project.author in request.user.person.subscriptions.all() else False
    return render(request, 'skillport/project.html', {
        'project': project, 
        'another': another, 
        'subscribed': subscribed, 
        'form': form,
        'comments': comments
        }
    )


def favorites_page(request):
    favorites = request.user.person.likes.order_by('-date')
    return render(request, 'skillport/favorites.html', {'favorites': favorites})


def subscriptions_page(request):
    subscriptions = request.user.person.subscriptions.order_by('user')
    return render(request, 'skillport/subscriptions.html', {'subscriptions': subscriptions})


def set_like(request):
    project = get_object_or_404(Project, id=request.POST.get('project_id'))
    if request.user.person not in project.likes.all():
        project.likes.add(request.user.person)
    else:
        project.likes.remove(request.user.person)
        
    return redirect('project', request.POST.get('project_id'))


def subscribe_from_project(request, project_id):
    user = get_object_or_404(Person, id=request.POST.get('user_id'))
    if user not in request.user.person.subscriptions.all():
        request.user.person.subscriptions.add(user)
    else:
        request.user.person.subscriptions.remove(user)
    
    return redirect('project', project_id)


def subscribe(request):
    user = get_object_or_404(Person, id=request.POST.get('user_id'))
    if user not in request.user.person.subscriptions.all():
        request.user.person.subscriptions.add(user)
    else:
        request.user.person.subscriptions.remove(user)
    
    return redirect('another_profile', request.POST.get('user_id'))


def unsubscribe(request):
    user = get_object_or_404(Person, id=request.POST.get('user_id'))
    print(user)
    request.user.person.subscriptions.remove(user)

    return redirect('subscriptions')