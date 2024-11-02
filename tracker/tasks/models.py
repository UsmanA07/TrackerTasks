from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    create = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create']

