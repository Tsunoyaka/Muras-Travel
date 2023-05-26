# Generated by Django 4.2.1 on 2023-05-26 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.RenameField(
            model_name='newsimages',
            old_name='tour',
            new_name='news',
        ),
        migrations.RenameField(
            model_name='newsvideos',
            old_name='tour',
            new_name='news',
        ),
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='tour_image', verbose_name='Главное изображение'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название новости'),
        ),
        migrations.AlterField(
            model_name='newsimages',
            name='image',
            field=models.ImageField(upload_to='news_images', verbose_name='Изображения'),
        ),
        migrations.AlterField(
            model_name='newsvideos',
            name='video',
            field=models.FileField(upload_to='news_videos', verbose_name='Видео'),
        ),
    ]