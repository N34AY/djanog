from django.db import models


class User(models.Model):
    site_id = models.CharField('SiteID', max_length=50)
    name = models.CharField('Name', max_length=50)
    sur_name = models.CharField('SurName', max_length=50)
    email = models.CharField('Email', max_length=50)
    phone = models.CharField('Phone', max_length=50)
    active = models.CharField('Active', max_length=1)
    password = models.CharField('Email', max_length=50)

    def __str__(self):
        return '{} {} {} {} {} {} {}'.format(self.site_id, self.name, self.sur_name, self.email, self.phone, self.active, self.password)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
