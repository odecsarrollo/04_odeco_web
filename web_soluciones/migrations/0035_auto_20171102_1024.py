# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-02 15:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_soluciones', '0034_auto_20171102_1001'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='itemsoluciontagseo',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='itemsoluciontagseo',
            name='item_solucion',
        ),
        migrations.DeleteModel(
            name='ItemSolucionTagSeo',
        ),
    ]
