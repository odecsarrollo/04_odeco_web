# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-02 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_soluciones', '0031_auto_20171102_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsolucion',
            name='alt_seo',
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
    ]