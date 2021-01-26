from django.db import models

class City(models.Model):

    # verbose_name='Города' - русификация добавления новых объяектов в админке
    # max_length=100 - максимальное колличество символов в названии
    # unique=True - уникальность названия
    name = models.CharField(max_length=100, unique=True, verbose_name='Города')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ['name']
