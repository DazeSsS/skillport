from django.db import models
import uuid


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default=None)
    tags = models.ManyToManyField('Tag', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    #comments = models.

    def __str__(self):
        return self.title
    

class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Comment(models.Model):
    VOTE_TYPE = [
        ('up', 'Вверх'),
        ('down', 'Вниз')
    ]
    text = models.TextField(blank=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    value = models.CharField(max_length=150, choices=VOTE_TYPE)
    date = models.DateTimeField(auto_now_add=True)
    #user = пока хз как описать отношения между пользователями и комментами
    
    def __str__(self):
        return self.value