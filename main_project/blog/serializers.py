from rest_framework import serializers
from .models import BlogPost, Todo

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id','title','content','published_at','user']


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['task','timestamp','completed','updated','user']