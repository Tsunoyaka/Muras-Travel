from django.urls import path

from .views import PhotoReportAPIVIew


urlpatterns = [
    path('get-photo-report/', PhotoReportAPIVIew.as_view(), name='get-tour'),

]



