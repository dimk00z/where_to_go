# Generated by Django 3.1.2 on 2020-10-28 06:16

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_auto_20201027_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='short_description',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Короткое описание'),
        ),
    ]
