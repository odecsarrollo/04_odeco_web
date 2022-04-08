# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-04-06 13:57
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields
import web_configurations.models


class Migration(migrations.Migration):

    dependencies = [
        ('web_configurations', '0035_laempresaconfiguration_video_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='laempresaconfiguration',
            name='imagen_info_empresa',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=web_configurations.models.LaEmpresaConfiguration.imagen_info_upload_to, verbose_name='Imagen Informacion Empresa (570x362)'),
        ),
        migrations.AddField(
            model_name='laempresaconfiguration',
            name='imagen_info_empresa_en',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=web_configurations.models.LaEmpresaConfiguration.imagen_info_upload_to, verbose_name='Imagen Informacion Empresa Ingles (570x362)'),
        ),
    ]