# Generated by Django 4.2.1 on 2023-05-26 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='image',
            field=models.ImageField(upload_to='tour_image', verbose_name='Главное изображение'),
        ),
        migrations.AlterField(
            model_name='tourimages',
            name='image',
            field=models.ImageField(upload_to='tour_images', verbose_name='Изображния'),
        ),
    ]
