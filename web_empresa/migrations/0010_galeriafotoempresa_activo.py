# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-27 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_empresa', '0009_auto_20171006_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='galeriafotoempresa',
            name='activo',
            field=models.BooleanField(default=False),
        ),
    ]
