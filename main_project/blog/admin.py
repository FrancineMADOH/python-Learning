from django.contrib import admin
from .models import BlogPost, Todo

# Register your models here.

admin.site.register(BlogPost)
admin.site.register(Todo)
