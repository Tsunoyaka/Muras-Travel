from django.contrib import admin
from .models import Tour, TourImages, ReportForm


class TabularInImages(admin.TabularInline):
    model = TourImages
    extra = 1
    fields = ['image']


class TourAdmin(admin.ModelAdmin):
    model = Tour
    inlines = [TabularInImages]



admin.site.register(Tour, TourAdmin)
admin.site.register(ReportForm)
