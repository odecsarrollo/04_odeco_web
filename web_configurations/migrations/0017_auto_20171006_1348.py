# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 18:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_configurations', '0016_auto_20171006_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cacheconfiguration',
            name='nombre_cache_index_header',
        ),
        migrations.RemoveField(
            model_name='cacheconfiguration',
            name='tiempo_cache_index_header',
        ),
    ]
