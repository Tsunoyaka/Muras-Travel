# Generated by Django 4.2.1 on 2023-05-26 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0002_alter_tour_image_alter_tourimages_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tour',
            options={'verbose_name': 'Тур', 'verbose_name_plural': 'Туры'},
        ),
        migrations.AlterField(
            model_name='tour',
            name='image',
            field=models.ImageField(upload_to='tour_images', verbose_name='Главное изображение'),
        ),
    ]
