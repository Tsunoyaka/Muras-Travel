from django.db import models
from .utils import normalize_phone

class Tour(models.Model):
    title = models.CharField(verbose_name='Название Тура', max_length=255)
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Стоимость')
    date = models.DateField(verbose_name='Дата тура')
    image = models.ImageField(verbose_name='Главное изображение',upload_to='tour_images')


    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'


    def __str__(self) -> str:
        return self.title


class TourImages(models.Model):
    tour = models.ForeignKey(to=Tour, on_delete=models.CASCADE, related_name='tour_carousel_img')
    image = models.ImageField(verbose_name='Изображния',upload_to='tour_images')

   
class ReportForm(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=55)
    phone = models.CharField(verbose_name='Номер', max_length=13)
    tour = models.ForeignKey(to=Tour, on_delete=models.CASCADE, related_name='report_form')

    def __str__(self) -> str:
        return f'{self.name} - {self.phone}'