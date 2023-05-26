# Generated by Django 4.2.1 on 2023-05-15 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название Тура')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
                ('date', models.DateField(verbose_name='Дата тура')),
                ('image', models.ImageField(upload_to='tour_image')),
            ],
        ),
        migrations.CreateModel(
            name='TourImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='tour_images')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tour_carousel_img', to='tour.tour')),
            ],
        ),
    ]