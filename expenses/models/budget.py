from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from .base import TimeStampedModel
from .expense_group import ExpenseGroup
from .category import Category

class Budget(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')
    group = models.ForeignKey(ExpenseGroup, on_delete=models.CASCADE, related_name='budgets')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='budgets')
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        unique_together = ['user', 'group', 'category', 'start_date', 'end_date']
        ordering = ['-start_date']

    def __str__(self):
        return f"Budget for {self.group.name} - {self.category.name if self.category else 'All Categories'}"