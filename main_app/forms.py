# delete this page?
# 
from django import forms
from .models import User, Post, Comment

class UserForm(forms.ModelForm):
    class Meta:      
        model = User
        fields = ("name", "username", "email")

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title","body","user")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("title","body","user", "post")
