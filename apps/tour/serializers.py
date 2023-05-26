from rest_framework import serializers
from django.db.models import Avg

from .models import Tour, TourImages


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ('title', 'description', 'price', 'date', 'image')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['carousel_img'] = TourImagesSerializer(instance.tour_carousel_img.all(), many=True).data
        return representation


class TourImagesSerializer(serializers.ModelSerializer):
    tour = serializers.StringRelatedField()

    class Meta:
        model = TourImages
        fields = ('tour', 'image')