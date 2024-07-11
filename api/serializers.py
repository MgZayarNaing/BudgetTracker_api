from rest_framework import serializers
from .models import Currency, IncomeCategory, ExpensesCategory, Income, Expense

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id', 'name']

class IncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeCategory
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'user']

class ExpensesCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpensesCategory
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'user']

class IncomeSerializer(serializers.ModelSerializer):
    category = IncomeCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=IncomeCategory.objects.all(), write_only=True, source='category')

    class Meta:
        model = Income
        fields = ['id', 'user', 'category', 'category_id', 'amount', 'description', 'date', 'created_at', 'updated_at']

class ExpenseSerializer(serializers.ModelSerializer):
    category = ExpensesCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=ExpensesCategory.objects.all(), write_only=True, source='category')

    class Meta:
        model = Expense
        fields = ['id', 'user', 'category', 'category_id', 'amount', 'description', 'date', 'created_at', 'updated_at']
