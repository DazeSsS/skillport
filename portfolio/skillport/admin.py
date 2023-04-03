from django.contrib import admin
from .models import Project, Tag, Comment

admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Comment)
