from django.db import models
from django.contrib.auth.models import User
from .base import TimeStampedModel

class Category(TimeStampedModel):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')

    class Meta:
        unique_together = ['user', 'name']
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name