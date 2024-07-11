from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from api.models import Income,Balance
from api.serializers import IncomeSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Sum

@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def income_list(request):
    incomes = Income.objects.filter(user=request.user)
    serializer = IncomeSerializer(incomes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def income_create(request):
    serializer = IncomeSerializer(data=request.data)
    if serializer.is_valid():
        income = serializer.save(user=request.user)
        balance, created = Balance.objects.get_or_create(user=request.user)
        balance.amount += income.amount
        balance.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def income_detail(request, pk):
    income = get_object_or_404(Income, pk=pk, user=request.user)
    serializer = IncomeSerializer(income)
    return Response(serializer.data)

@api_view(['PUT'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def income_update(request, pk):
    income = get_object_or_404(Income, pk=pk, user=request.user)
    serializer = IncomeSerializer(income, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def income_delete(request, pk):
    income = get_object_or_404(Income, pk=pk)
    balance = Balance.objects.get(user=request.user)
    balance.amount -= income.amount
    balance.save()
    income.delete()
    return Response({"detail": "Income deleted successfully."}, status=status.HTTP_200_OK)

@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def total_income(request):
    total = Income.objects.filter(user=request.user).aggregate(total_amount=Sum('amount'))
    return Response(total)