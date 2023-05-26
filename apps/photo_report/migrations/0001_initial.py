# Generated by Django 4.2.1 on 2023-05-26 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')),
                ('image', models.ImageField(upload_to='photo_report_images', verbose_name='Главное изображение')),
            ],
            options={
                'verbose_name': 'Фотоотчёт',
                'verbose_name_plural': 'Фотоотчёты',
            },
        ),
        migrations.CreateModel(
            name='ReportImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='report_images', verbose_name='Изображения')),
                ('photo_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_carousel_img', to='photo_report.photoreport')),
            ],
        ),
    ]