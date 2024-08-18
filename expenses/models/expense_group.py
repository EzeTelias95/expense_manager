from django.db import models
from django.contrib.auth.models import User
from .base import TimeStampedModel

class ExpenseGroup(TimeStampedModel):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expense_groups')

    class Meta:
        unique_together = ['user', 'name']
        ordering = ['name']

    def __str__(self):
        return self.name