from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length = 100)
    profile_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = CharField(max_length = 250)
    body = TextField(max_length = 1000)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    def __str__(self):
        return self.title
