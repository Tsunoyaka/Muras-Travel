from rest_framework import serializers

from .models import News, NewsImages, NewsVideos


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'description', 'created_at', 'image')

    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        representation['carousel_img'] = NewsImagesSerializer(instance.news_carousel_img.all(), many=True).data
        representation['carousel_videos'] = NewsVideosSerializer(instance.news_carousel_videos.all(), many=True).data
        return representation




class NewsImagesSerializer(serializers.ModelSerializer):
    news = serializers.StringRelatedField()

    class Meta:
        model = NewsImages
        fields = ('news', 'image')


class NewsVideosSerializer(serializers.ModelSerializer):
    news = serializers.StringRelatedField()

    class Meta:
        model = NewsVideos
        fields = ('news', 'video')



