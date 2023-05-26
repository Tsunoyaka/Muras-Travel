from django.db import models


class News(models.Model):
    title = models.CharField(verbose_name='Название новости', max_length=255)
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(verbose_name='Дата загрузки',auto_now_add=True)
    image = models.ImageField(verbose_name='Главное изображение', upload_to='tour_image')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


    def __str__(self) -> str:
        return self.title


class NewsImages(models.Model):
    news = models.ForeignKey(to=News, on_delete=models.CASCADE, related_name='news_carousel_img')
    image = models.ImageField(verbose_name='Изображения', upload_to='news_images')


class NewsVideos(models.Model):
    news = models.ForeignKey(to=News, on_delete=models.CASCADE, related_name='news_carousel_videos')
    video = models.FileField(verbose_name='Видео', upload_to='news_videos')


