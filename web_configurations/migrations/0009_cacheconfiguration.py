# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_configurations', '0008_auto_20171005_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='CacheConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cache_empresa', models.CharField(default='cache inicial empresa', help_text='Cambiar por cada cambio en Empresa, Aliados o Galeria Empresa', max_length=10, verbose_name='Nombre del cache empresa')),
                ('nombre_cache_clientes', models.CharField(default='cache inicial clientes', help_text='Cambiar por cada cambio en Clientes', max_length=10, verbose_name='Nombre del cache clientes')),
            ],
            options={
                'verbose_name': 'Cache',
            },
        ),
    ]
