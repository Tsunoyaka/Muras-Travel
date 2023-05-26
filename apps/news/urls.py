from django.urls import path

from .views import NewsAPIVIew


urlpatterns = [
    path('get-news/', NewsAPIVIew.as_view(), name='get-news'),

]



