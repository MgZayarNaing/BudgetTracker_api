# views/expense_views.py
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from api.models import Expense,Balance
from api.serializers import ExpenseSerializer, ExpensesCategorySerializer

@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def expense_create(request):
    serializer = ExpenseSerializer(data=request.data)
    if serializer.is_valid():
        expense = serializer.save(user=request.user)
        balance, created = Balance.objects.get_or_create(user=request.user)
        balance.amount -= expense.amount
        balance.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def expense_detail(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    serializer = ExpenseSerializer(expense)
    return Response(serializer.data)

@api_view(['PUT'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def expense_update(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    serializer = ExpenseSerializer(expense, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    balance = Balance.objects.get(user=request.user)
    balance.amount += expense.amount
    balance.save()
    expense.delete()
    return Response({"detail": "Expense deleted successfully."}, status=status.HTTP_200_OK)

@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def total_expense(request):
    total = Expense.objects.filter(user=request.user).aggregate(total_amount=Sum('amount'))
    return Response(total)
