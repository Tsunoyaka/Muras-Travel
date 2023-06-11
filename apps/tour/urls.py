from django.urls import path

from .views import TourAPIVIew, ReportFormAPIView


urlpatterns = [
    path('get-tour/', TourAPIVIew.as_view(), name='get-tour'),
    path('report-form/', ReportFormAPIView.as_view(), name='report-form'),
]



