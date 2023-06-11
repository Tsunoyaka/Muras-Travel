from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .models import Tour
from .serializers import TourSerializer, ReportFormSerializer



class TourAPIVIew(APIView):

    def get(self, request):
        queryset = Tour.objects.all()
        serializer = TourSerializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    
class ReportFormAPIView(APIView):

    @swagger_auto_schema(request_body=ReportFormSerializer)
    def post(self, request):
        serializer = ReportFormSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                'Форма заполнена успешно!',
                status=status.HTTP_201_CREATED
            )