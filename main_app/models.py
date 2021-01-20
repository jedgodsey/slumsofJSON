from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length = 100)
    profile_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 250)
    body = models.TextField(max_length = 1000)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    def __str__(self):
        return self.title

class Comment(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField(max_length = 500)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
