# Generated by Django 4.0.4 on 2022-04-14 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_soluciones', '0058_itemsolucionimagen_slug_itemsolucionimagen_slug_en'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemsolucionimagen',
            name='slug_en',
        ),
    ]
