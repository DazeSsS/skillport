from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import CreateUserForm


class ProjectInline(admin.TabularInline):
    model = Project


@admin.register(Person)
class UserAdmin(UserAdmin):
    model = Person
    list_display = ['username', 'id', 'email', 'first_name', 'last_name']
    inlines = [ProjectInline]


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ['id', 'title', 'description', 'date', 'author', 'content_type']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['body', 'project', 'created', 'author']
    list_filter = ['created']
    search_fields = ['body']

admin.site.register(ProjectType)