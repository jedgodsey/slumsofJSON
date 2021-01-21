from django import forms
from .models import Profile, Post, Comment

class ProfileForm(forms.ModelForm):
    class Meta:      
        model = Profile
        fields = ("name", "profile_name", "email")

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title","body","profile")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("title","body","profile", "post")
