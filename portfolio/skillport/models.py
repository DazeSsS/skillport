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

    def __str__(self):
        return self.username


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # image = models.ImageField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='projects')
    content_type = models.ForeignKey('ProjectType', on_delete=models.PROTECT)

    def __str__(self):
        return self.title
    

class ProjectType(models.Model):
    name = models.CharField(max_length=30, db_index=True)

    def __str__(self):
        return self.name


# class Comment(models.Model):
#     VOTE_TYPE = [
#         ('up', 'Вверх'),
#         ('down', 'Вниз')
#     ]
#     text = models.TextField(blank=False)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     value = models.CharField(max_length=150, choices=VOTE_TYPE)
#     date = models.DateTimeField(auto_now_add=True)
#     #user = пока хз как описать отношения между пользователями и комментами
    
#     def __str__(self):
#         return self.value