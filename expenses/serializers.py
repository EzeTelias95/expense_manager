from rest_framework import serializers
from .models import Budget, Expense, Category, ExpenseGroup

class ExpenseGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseGroup
        fields = ['id', 'name']

class ExpenseSerializer(serializers.ModelSerializer):
    groups = ExpenseGroupSerializer(many=True, read_only=True)
    group_ids = serializers.PrimaryKeyRelatedField(many=True, write_only=True, queryset=ExpenseGroup.objects.all(), source='groups')

    class Meta:
        model = Expense
        fields = ['id', 'amount', 'description', 'date', 'category', 'groups', 'group_ids']

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'amount', 'start_date', 'end_date', 'group', 'category']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']