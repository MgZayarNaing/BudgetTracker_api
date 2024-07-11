from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from api.models import Balance

@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def get_balance(request):
    try:
        balance = Balance.objects.get(user=request.user)
        return Response({"balance": balance.amount}, status=status.HTTP_200_OK)
    except Balance.DoesNotExist:
        return Response({"balance": 0}, status=status.HTTP_200_OK)
