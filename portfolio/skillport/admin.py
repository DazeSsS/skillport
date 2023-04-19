from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from .models import *

@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ['id', 'title', 'description', 'date', 'author', 'content_type', 'likes']

admin.site.register(Person, UserAdmin)
admin.site.register(ProjectType)
