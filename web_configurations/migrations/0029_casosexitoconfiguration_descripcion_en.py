# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-09 15:55
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('web_configurations', '0028_auto_20180109_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='casosexitoconfiguration',
            name='descripcion_en',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Texto Casos Éxito Ingles'),
        ),
    ]