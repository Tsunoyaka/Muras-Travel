from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .models import Tour
from .serializers import TourSerializer



class TourAPIVIew(APIView):

    swagger_auto_schema(request_body=TourSerializer)
    def get(self, request):
        queryset = Tour.objects.all()
        serializer = TourSerializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    