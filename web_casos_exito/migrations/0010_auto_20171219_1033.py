# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-19 15:33
from __future__ import unicode_literals

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web_casos_exito', '0009_casoexitotestimonio_cargo'),
    ]

    operations = [
        migrations.AddField(
            model_name='casoexito',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='casoexito',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
    ]
