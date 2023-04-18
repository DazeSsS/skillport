from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import Person, Project

class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'login'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'surname'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'name'}))
    specialization = forms.CharField(widget=forms.TextInput(attrs={'class': 'specialization'}))
    links = forms.CharField(widget=forms.TextInput(attrs={'class': 'links'}))
    about = forms.CharField(widget=forms.Textarea(attrs={'class': 'about'}))

    class Meta:
        model = Person
        fields = ('username', 'email', 'password1', 'password2', 'last_name', 'first_name', 'specialization', 'links', 'about')


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'