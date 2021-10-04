from django.db import models
# Create your models here.


class Hero (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    identity = models.TextField(max_length=300, default="hi")
    strength = models.TextField(max_length=300, default="hi")
    weakness = models.TextField(max_length=300, default="hi")
    image = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}, {self.description}"
