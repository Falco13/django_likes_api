from django.contrib import admin
from likes_api.models import Post, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'author', 'created_at', 'get_likes']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'liker', 'post', 'created_at']
