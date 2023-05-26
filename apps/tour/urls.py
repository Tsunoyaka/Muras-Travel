from django.urls import path

from .views import TourAPIVIew


urlpatterns = [
    path('get-tour/', TourAPIVIew.as_view(), name='get-tour'),

]



