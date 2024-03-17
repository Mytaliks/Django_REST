from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    name = models.CharField(max_length=64)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create = models.DateTimeField()

    def __str__(self):
        return self.name