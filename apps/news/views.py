from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .models import News
from .serializers import NewsSerializer



class NewsAPIVIew(APIView):

    swagger_auto_schema(request_body=NewsSerializer)
    def get(self, request):
        queryset = News.objects.all()
        serializer = NewsSerializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    