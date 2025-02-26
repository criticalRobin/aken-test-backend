from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    time = models.CharField(max_length=50)
    summary = models.TextField()

    def __str__(self):
        return self.title
