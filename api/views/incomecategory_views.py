from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from api.models import IncomeCategory
from api.serializers import IncomeCategorySerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def income_category_list(request):
    categories = IncomeCategory.objects.filter(user=request.user)
    serializer = IncomeCategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def income_category_create(request):
    serializer = IncomeCategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def income_category_detail(request, pk):
    category = get_object_or_404(IncomeCategory, pk=pk)
    serializer = IncomeCategorySerializer(category)
    return Response(serializer.data)

@api_view(['PUT'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def income_category_update(request, pk):
    category = get_object_or_404(IncomeCategory, pk=pk)
    serializer = IncomeCategorySerializer(category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def income_category_delete(request, pk):
    category = get_object_or_404(IncomeCategory, pk=pk)
    category.delete()
    return Response({"detail": "Income category deleted successfully."}, status=status.HTTP_200_OK)
