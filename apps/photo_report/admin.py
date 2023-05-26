from django.contrib import admin
from .models import PhotoReport, ReportImages

class TabularInImages(admin.TabularInline):
    model = ReportImages
    extra = 1
    fields = ['image']


class TourAdmin(admin.ModelAdmin):
    model = PhotoReport
    inlines = [TabularInImages]



admin.site.register(PhotoReport, TourAdmin)
