from django.contrib import admin
from .models import *

admin.site.register(Person)
admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Comment)
