# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_configurations', '0004_auto_20170925_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalconfiguration',
            name='facebook',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='generalconfiguration',
            name='instagram',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='generalconfiguration',
            name='twitter',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='generalconfiguration',
            name='youtube',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]