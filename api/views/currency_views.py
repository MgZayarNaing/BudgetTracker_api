from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from api.models import Currency
from api.serializers import CurrencySerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def currency_list(request):
    currencies = Currency.objects.all()
    serializer = CurrencySerializer(currencies, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@renderer_classes([JSONRenderer])
@permission_classes([AllowAny])
def currency_create(request):
    serializer = CurrencySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def currency_detail(request, pk):
    currency = get_object_or_404(Currency, pk=pk)
    serializer = CurrencySerializer(currency)
    return Response(serializer.data)

@api_view(['PUT'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def currency_update(request, pk):
    currency = get_object_or_404(Currency, pk=pk)
    serializer = CurrencySerializer(currency, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def currency_delete(request, pk):
    currency = get_object_or_404(Currency, pk=pk)
    currency.delete()
    return Response({"detail": "Currency deleted successfully."}, status=status.HTTP_200_OK)
