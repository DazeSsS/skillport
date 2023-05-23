from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import *


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'id', 'email', 'first_name', 'last_name')


@admin.register(Person)
class PersonAdmin(ModelAdmin):
    list_display = ['user', 'guest_name', 'id', 'specialization', 'links', 'about', 'profile_picture']


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ['id', 'title', 'description', 'date', 'author', 'content_type']


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ['project', 'author', 'body',  'created']


@admin.register(AdditionalImages)
class AdditionalImageAdmin(ModelAdmin):
    list_display = ['project']


@admin.register(AttachedFiles)
class AttachedFileAdmin(ModelAdmin):
    list_display = ['project']


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(ProjectType)