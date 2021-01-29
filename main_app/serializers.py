from rest_framework import serializers
from models import Profile, Post, Comment

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:      
        model = Profile
        fields = ("name", "profile_name", "email")

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title","body","profile")

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("title","body","profile", "post")
