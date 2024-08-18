from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from .base import TimeStampedModel
from .expense_group import ExpenseGroup
from .category import Category

class Expense(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    group = models.ForeignKey(ExpenseGroup, on_delete=models.CASCADE, related_name='expenses')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    description = models.CharField(max_length=255)
    date = models.DateField()

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.description} - {self.amount}"