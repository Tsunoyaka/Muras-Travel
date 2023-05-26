from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .models import PhotoReport
from .serializers import PhotoReportSerializer



class PhotoReportAPIVIew(APIView):

    swagger_auto_schema(request_body=PhotoReportSerializer)
    def get(self, request):
        queryset = PhotoReport.objects.all()
        serializer = PhotoReportSerializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    