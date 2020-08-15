from django.db import models


class Stats(models.Model):
    date = models.DateTimeField('Date', max_length=100)
    man = models.CharField('Man', max_length=50)
    girl = models.CharField('Girl', max_length=50)
    partner = models.CharField('Partner', max_length=50)
    partner_get = models.CharField('Partner_get', max_length=10)
    name = models.CharField('Name', max_length=100)
    comment = models.CharField('Comment', max_length=100)

    def __str__(self):
        return '{} {} {} {} {} {} {}'.format(self.date, self.man, self.girl, self.partner, self.partner_get, self.name, self.comment)

    class Meta:
        verbose_name = 'Запись статистики'
        verbose_name_plural = 'Статистика'
