from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
    
    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({'class': 'login'})
        self.fields['email'].widget.attrs.update({'class': 'email'})
        self.fields['password1'].widget.attrs.update({'class': 'password'})
        self.fields['password2'].widget.attrs.update({'class': 'password'})
        self.fields['last_name'].widget.attrs.update({'class': 'surname'})
        self.fields['first_name'].widget.attrs.update({'class': 'name'})


class CreatePersonForm(ModelForm):

    class Meta:
        model = Person
        fields = ['specialization', 'links', 'about', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['specialization'].widget.attrs.update({'class': 'specialization'})
        self.fields['links'].widget.attrs.update({'class': 'links'})
        self.fields['about'].widget.attrs.update({'class': 'about'})
        self.fields['profile_picture'].widget.attrs.update({
            'type': 'file', 
            'name': 'profilePicture',
            'id': 'imageUpload',
            'onchange': 'previewImage(event)',
            'accept': 'image/*'
        })


class CreateProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'content_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'input title'})
        self.fields['description'].widget.attrs.update({'class': 'input description-input'})
        self.fields['image'].widget.attrs.update({
            'class': 'input-button',
             'type': 'file', 
            'name': 'profilePicture',
            'id': 'imageUpload',
            'onchange': 'previewImage(event)',
            'accept': 'image/*'
            })
        self.fields['content_type'].widget.attrs.update({'class': 'dropdown__menu'})


class CreateCommentForm(ModelForm):
    
    class Meta:
        model = Comment
        fields = ['body']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['body'].widget.attrs.update({'class': 'input comment'})


class CreateAdditionalImageForm(ModelForm):
    additional_image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={"multiple": True, "class": "input-button"})
        )

    class Meta:
        model = AdditionalImages
        fields = ["additional_image"]


class CreateAttachedFileForm(ModelForm):
    attached_file = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(attrs={"multiple": True, "class": "input-button"})
        )

    class Meta:
        model = AdditionalImages
        fields = ["attached_file"]
