# Generated by Django 2.2.14 on 2020-07-05 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='date',
            field=models.CharField(max_length=100, verbose_name='Date'),
        ),
    ]