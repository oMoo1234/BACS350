from django.db import models
from django.urls.base import reverse_lazy

# Create your models here.


class Hero (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    identity = models.TextField(max_length=300, default="")
    strength = models.TextField(max_length=300, default="")
    weakness = models.TextField(max_length=300, default="")
    image = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}, {self.description}"

    def get_absolute_url(self):
        return reverse_lazy('add_hero')
