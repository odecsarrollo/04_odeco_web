# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-04-06 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_configurations', '0034_generalconfiguration_copyright'),
    ]

    operations = [
        migrations.AddField(
            model_name='laempresaconfiguration',
            name='video_en',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
