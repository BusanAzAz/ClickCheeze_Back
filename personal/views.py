from .models import Image
from .serializers import ImageSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['POST'])
def post(request):
    if request.method == 'POST':
        serializer = ImageSerializer (data=request.data)
        if serializer.is_valid(raise_exception = True):
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
