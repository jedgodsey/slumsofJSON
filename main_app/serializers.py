from rest_framework import serializers
from .models import Profile, Post, Comment

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:      
        model = Profile
        fields = '__all__'
        # fields = ("name", "profile_name", "email")

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ("title","body","profile")

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        # fields = ("title","body","profile", "post")
