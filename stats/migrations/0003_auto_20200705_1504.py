# Generated by Django 2.2.14 on 2020-07-05 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_auto_20200705_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='date',
            field=models.DateTimeField(max_length=100, verbose_name='Date'),
        ),
    ]
