
from django.db import models


class Article(models.Model):
    creator = models.CharField(max_length=50, null=True, blank=True)
    tag = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    content = models.TextField()
