from django.db import models

class Mc(models.Model):
    name = models.CharField(max_length = 100)
    mc_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    def __str__(self):
        return self.name
