from django.db import models

# Create your models here.


class Place(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название локации'
    )
    description_short = models.TextField(
        max_length=400,
        verbose_name='Короткое описание'
    )
    description_long = models.TextField(verbose_name='Длинное описание')
    lng = models.DecimalField(
        max_digits=16,
        decimal_places=14,
        verbose_name='Долгота'
    )
    lat = models.DecimalField(
        max_digits=16,
        decimal_places=14,
        verbose_name='Широта'
    )

    def __str__(self):
        return f'{self.id}. {self.title}'


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Название локации',
    )
    image = models.ImageField()
    title = models.CharField(
        max_length=100,
        verbose_name='Название картинки'
    )

    number = models.PositiveIntegerField(
        default=0, verbose_name='Позиция', db_index=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f'{self.number}. {self.title}'
