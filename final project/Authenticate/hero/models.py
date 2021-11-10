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
        return reverse_lazy('hero_list')


class Article(models.Model):
    title = models.CharField(max_length=200)
    story = models.TextField(max_length=400)

    def export_record(self):
        return [self.story, self.title]

    # @staticmethod
    # def import_record(values):
    #     c = Article.objects.get_or_create(book=values[0], order=values[1])[0]
    #     c.title = values[2]
    #     c.save()
    #     return c

    # def __str__(self):
    #     return f'{ self.book.title} - {self.order} - {self.title}'
