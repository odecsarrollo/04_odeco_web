# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_configurations', '0013_auto_20171006_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='cacheconfiguration',
            name='empresa_update',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
