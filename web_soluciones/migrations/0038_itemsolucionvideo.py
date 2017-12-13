# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-29 15:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_soluciones', '0037_auto_20171102_1035'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemSolucionVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.CharField(blank=True, max_length=500, null=True)),
                ('orden', models.PositiveIntegerField(default=0)),
                ('item_solucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mis_videos', to='web_soluciones.ItemSolucion')),
            ],
        ),
    ]