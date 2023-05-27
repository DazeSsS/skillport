from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import uuid
import os


def user_media_path(instance, filename):
    return '{0}/profile/{1}'.format(instance.user, filename)


def project_media_path(instance, filename):
    return '{0}/project_{1}/{2}'.format(instance.author, instance.title.strip().replace(' ', '-'), filename)


def additional_media_path(instance, filename):
    return '{0}/project_{1}/{2}'.format(instance.project.author, instance.project.title.strip().replace(' ', '-'), filename)


class Person(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100, blank=True)
    links = models.TextField(blank=True)
    about = models.TextField(blank=True)
    profile_picture = models.ImageField(blank=True, upload_to=user_media_path, default="default/default_pfp.png")
    subscriptions = models.ManyToManyField('self', blank=True)
    device = models.CharField(max_length=200, null=True, blank=True)
    guest_name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        if self.user:
            return self.user.username
        else:
            return f'{self.guest_name}'

    def get_subscriptions_count(self):
        count = str(self.subscriptions.count())
        if count[-1] == '1' and count != '11':
            return f'{count} Подписчик'
        elif count[-1] in ['2', '3', '4'] and count not in ['12', '13', '14']:
            return f'{count} Подписчика'
        else:
            return f'{count} Подписчиков'


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to=project_media_path, default="default/default_pfp.png")
    content_type = models.ForeignKey('ProjectType', on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='projects')
    likes = models.ManyToManyField('Person', blank=True, related_name='likes')

    def __str__(self):
        return self.title
    
    def get_comments_count(self):
        count = str(self.comments.count())
        if count[-1] == '1' and count != '11':
            return f'{count} комментарий'
        elif count[-1] in ['2', '3', '4'] and count not in ['12', '13', '14']:
            return f'{count} комментария'
        else:
            return f'{count} комментариев'
    

class ProjectType(models.Model):
    name = models.CharField(max_length=30, db_index=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    project = models.ForeignKey('Project', related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey('Person', null=True, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body
    
class AdditionalImages(models.Model):
    project = models.ForeignKey(Project, related_name="additional_images", on_delete=models.CASCADE)
    additional_image = models.ImageField(blank=True, upload_to=additional_media_path, default="default/default_pfp.png")


class AttachedFiles(models.Model):
    project = models.ForeignKey(Project, related_name="attached_files", on_delete=models.CASCADE)
    attached_file = models.FileField(blank=True, upload_to=additional_media_path, default="default/default_pfp.png")

    def filename(self):
        return os.path.basename(self.attached_file.name)