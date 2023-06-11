from rest_framework import serializers
from django.db.models import Avg

from .models import Tour, TourImages, ReportForm
from .utils import normalize_phone
from .tasks import send_report_form

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


class ReportFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportForm
        fields = ('name', 'phone', 'tour')
    
    def validate_phone(self, phone):
        phone = normalize_phone(phone)
        if len(phone) != 13:
            raise serializers.ValidationError('Неверный формат телефона')
        return phone
    
    def create(self, validated_data):
        send_report_form.delay(name=validated_data['name'], phone=validated_data['phone'], 
                        tour=validated_data['tour'])
        return super().create(validated_data)