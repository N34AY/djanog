# Generated by Django 2.2.14 on 2020-07-05 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_id', models.CharField(max_length=50, verbose_name='SiteID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('sur_name', models.CharField(max_length=50, verbose_name='SurName')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone')),
                ('active', models.CharField(max_length=1, verbose_name='Active')),
            ],
            options={
                'verbose_name_plural': 'Пользователи',
                'verbose_name': 'Пользователь',
            },
        ),
    ]
