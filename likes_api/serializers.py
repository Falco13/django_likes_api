from rest_framework import serializers
from likes_api.models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'author', 'created_at', 'likes']

    def get_likes(self, post):
        return Like.objects.filter(post=post).count()


class LikeSerializer(serializers.ModelSerializer):
    liker = serializers.ReadOnlyField(source='liker.username')

    class Meta:
        model = Like
        fields = ['id', 'liker', 'created_at']
