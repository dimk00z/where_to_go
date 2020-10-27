from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from tinymce import models as tinymce_models
# Create your models here.


class Place(models.Model):
    point_title = models.CharField(
        max_length=100,
        verbose_name='Название точки',
        help_text='При наведении курсором на точку будет отображаться это название.'
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Название локации',
        help_text='Заголовок в описании.'
    )
    short_description = tinymce_models.HTMLField(
        max_length=400,
        blank=True,
        verbose_name='Короткое описание'
    )
    long_description = tinymce_models.HTMLField(
        blank=True,
        verbose_name='Длинное описание')
    lng = models.DecimalField(
        max_digits=17,
        decimal_places=15,
        verbose_name='Долгота'
    )
    lat = models.DecimalField(
        max_digits=17,
        decimal_places=15,
        verbose_name='Широта'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('place_detail', args=[self.id])


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Название локации',
        related_name='images'
    )
    image = models.ImageField()

    number = models.PositiveIntegerField(
        default=0, verbose_name='Порядковый номер',  db_index=True)

    def get_preview_image(self):
        if self.image.url:
            return format_html('<img src="{}" height="200"/>',
                               self.image.url,
                               )
        return 'Место для превью файла'

    get_preview_image.short_description = 'Предизображение'

    def __str__(self):
        return f'{self.number} - {self.place}'

    class Meta:
        ordering = ['number']
