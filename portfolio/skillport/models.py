from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

import uuid


class Person(AbstractUser):
    email = models.EmailField(_("email address"), blank=False, unique=True)
    specialization = models.CharField(max_length=100, blank=True)
    links = models.TextField(blank=True)
    about = models.TextField(blank=True)
    profile_picture = models.ImageField(blank=True, upload_to="images/%Y/%m/%d/", default="img/default_pfp.png")

    def __str__(self):
        return self.username

User = get_user_model()

class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to="images/%Y/%m/%d/")
    content_type = models.ForeignKey('ProjectType', on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    likes = models.ManyToManyField(User, related_name='likes')

    def __str__(self):
        return self.title
    

class ProjectType(models.Model):
    name = models.CharField(max_length=30, db_index=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Person, null=True, on_delete=models.CASCADE, related_name='user')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.body