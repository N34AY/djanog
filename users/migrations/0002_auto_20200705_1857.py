# Generated by Django 2.2.14 on 2020-07-05 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='def', max_length=50, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='def', max_length=50, verbose_name='Email'),
        ),
    ]
