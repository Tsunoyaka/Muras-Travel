from django.db import models


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

   