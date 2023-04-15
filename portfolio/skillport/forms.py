from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Project

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'login'
        self.fields['email'].widget.attrs['class'] = 'email'
        self.fields['password1'].widget.attrs['class'] = 'password'
        self.fields['password2'].widget.attrs['class'] = 'password'


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'