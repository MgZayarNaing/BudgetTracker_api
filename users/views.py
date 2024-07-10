from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status, filters
from .models import CustomUser
from .serializers import (
    CustomUserSerializer,
    CustomUserRegisterSerializer,
)
from .pagination import CustomUserPagination
from django.shortcuts import get_object_or_404

@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def user_list(request):
    users = CustomUser.objects.all()
    ordering = request.query_params.get('ordering', 'uuid')
    if ordering:
        users = users.order_by(ordering)
    paginator = CustomUserPagination()
    paginated_users = paginator.paginate_queryset(users, request)
    serializer = CustomUserSerializer(paginated_users, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['POST'])
@renderer_classes([JSONRenderer])
@permission_classes([AllowAny])
def user_create(request):
    serializer = CustomUserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def user_detail(request, pk):
    user = get_object_or_404(CustomUser, uuid=pk)
    serializer = CustomUserSerializer(user)
    return Response(serializer.data)

@api_view(['PUT'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def user_update(request, pk):
    user = get_object_or_404(CustomUser, uuid=pk)
    serializer = CustomUserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def user_delete(request, pk):
    user = get_object_or_404(CustomUser, uuid=pk)
    user.delete()
    return Response({"detail": "User deleted successfully."}, status=status.HTTP_200_OK)

