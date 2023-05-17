from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import Person, Project, Comment

class CreateUserForm(UserCreationForm):

    class Meta:
        model = Person
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name', 'specialization', 'links', 'about', 'profile_picture']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({'class': 'login'})
        self.fields['email'].widget.attrs.update({'class': 'email'})
        self.fields['password1'].widget.attrs.update({'class': 'password'})
        self.fields['password2'].widget.attrs.update({'class': 'password'})
        self.fields['last_name'].widget.attrs.update({'class': 'surname'})
        self.fields['first_name'].widget.attrs.update({'class': 'name'})
        self.fields['specialization'].widget.attrs.update({'class': 'specialization'})
        self.fields['links'].widget.attrs.update({'class': 'links'})
        self.fields['about'].widget.attrs.update({'class': 'about'})


class CreateProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'content_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'input name-input'})
        self.fields['description'].widget.attrs.update({'class': 'input description-input'})


class CreateCommentForm(ModelForm):
    
    class Meta:
        model = Comment
        fields = ['body']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['body'].widget.attrs.update({'class': 'input comment'})
