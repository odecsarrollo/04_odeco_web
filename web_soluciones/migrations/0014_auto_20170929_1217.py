# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_soluciones', '0013_auto_20170929_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solucion',
            name='descripcion_corta',
            field=models.TextField(blank=True, null=True),
        ),
    ]
