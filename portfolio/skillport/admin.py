from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from .models import *


class ProjectInline(admin.TabularInline):
    model = Project


@admin.register(Person)
class UserAdmin(UserAdmin):
    list_display = ['username', 'id', 'email', 'first_name', 'last_name']
    inlines = [ProjectInline]


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ['id', 'title', 'description', 'date', 'author', 'content_type']


admin.site.register(ProjectType)