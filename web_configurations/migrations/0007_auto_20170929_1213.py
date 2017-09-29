# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 17:13
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields
import web_configurations.models


class Migration(migrations.Migration):

    dependencies = [
        ('web_configurations', '0006_auto_20170928_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexconfiguration',
            name='header_imagen',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=web_configurations.models.IndexConfiguration.header_imagen_upload_to, verbose_name='Imagen Cabezote (2560 x 588)'),
        ),
        migrations.AlterField(
            model_name='laempresaconfiguration',
            name='imagen_principal',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=web_configurations.models.LaEmpresaConfiguration.imagen_principal_upload_to, verbose_name='Imagen Principal (570x362)'),
        ),
    ]
