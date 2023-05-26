from rest_framework import serializers

from .models import PhotoReport, ReportImages


class PhotoReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoReport
        fields = ('title', 'created_at', 'image')

    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        representation['carousel_img'] = ReportImagesSerializer(instance.report_carousel_img.all(), many=True).data
        return representation


class ReportImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportImages
        fields = ('photo_report', 'image')




