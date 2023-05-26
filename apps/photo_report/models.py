from django.db import models


class PhotoReport(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    created_at = models.DateTimeField(verbose_name='Дата загрузки', auto_now_add=True)
    image = models.ImageField(verbose_name='Главное изображение', upload_to='photo_report_images')

    class Meta:
        verbose_name = 'Фотоотчёт'
        verbose_name_plural = 'Фотоотчёты'



class ReportImages(models.Model):
    photo_report = models.ForeignKey(to=PhotoReport, on_delete=models.CASCADE, related_name='report_carousel_img')
    image = models.ImageField(verbose_name='Изображения', upload_to='report_images')



