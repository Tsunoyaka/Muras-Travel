# Generated by Django 4.2.1 on 2023-06-08 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0004_alter_tour_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, verbose_name='Имя')),
                ('phone', models.CharField(max_length=13, verbose_name='Номер')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_form', to='tour.tour')),
            ],
        ),
    ]
