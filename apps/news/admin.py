from django.contrib import admin
from .models import News, NewsImages, NewsVideos


class TabularInImages(admin.TabularInline):
    model = NewsImages
    extra = 1
    fields = ['image']


class TabularInVideos(admin.TabularInline):
    model = NewsVideos
    extra = 1
    fields = ['video']


class NewsAdmin(admin.ModelAdmin):
    model = News
    inlines = [TabularInImages, TabularInVideos]

admin.site.register(News, NewsAdmin)
