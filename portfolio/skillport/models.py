from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

import uuid


def user_media_path(instance, filename):
    return 'user_{0}/profile/{1}'.format(instance.user.id, filename)


def project_media_path(instance, filename):
    return 'user_{0}/project_{1}/{2}'.format(instance.author.id, instance.title.strip().replace(' ', '-'), filename)


class Person(AbstractUser):
    email = models.EmailField(_("email address"), blank=False, unique=True)
    specialization = models.CharField(max_length=100, blank=True)
    links = models.TextField(blank=True)
    about = models.TextField(blank=True)
    profile_picture = models.ImageField(blank=True, upload_to=user_media_path, default="default/default_pfp.png")
    subscriptions = models.ManyToManyField('self')

    def __str__(self):
        return self.username

    def get_subscriptions_count(self):
        count = str(self.subscriptions.count())
        print(count)
        if count[-1] == '1' and count != '11':
            return f'{count} Подписчик'
        elif count[-1] in ['2', '3', '4'] and count not in ['12', '13', '14']:
            return f'{count} Подписчика'
        else:
            return f'{count} Подписчиков'

User = get_user_model()


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to=project_media_path, default="default/default_pfp.png")
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
    project = models.ForeignKey(Project, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(Person, null=True, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.body