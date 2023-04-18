from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import Person, Project

class CreateUserForm(UserCreationForm):

    class Meta:
        model = Person
        fields = ('username', 'email', 'password1', 'password2', 'last_name', 'first_name', 'specialization', 'links', 'about')
    
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'login'
        self.fields['email'].widget.attrs['class'] = 'email'
        self.fields['password1'].widget.attrs['class'] = 'password'
        self.fields['password2'].widget.attrs['class'] = 'password'
        self.fields['last_name'].widget.attrs['class'] = 'surname'
        self.fields['first_name'].widget.attrs['class'] = 'name'
        self.fields['specialization'].widget.attrs['class'] = 'specialization'
        self.fields['links'].widget.attrs['class'] = 'links'
        self.fields['about'].widget.attrs['class'] = 'about'


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'