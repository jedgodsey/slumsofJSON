from django.db import models

class User(models.Model):
    name = models.Charfield(max_length = 100)
    username = models.Charfield(max_length = 100)
    email = models.Charfield(max_length = 100)
    def __str__(self):
        return self.name
