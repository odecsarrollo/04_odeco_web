# Generated by Django 4.0.4 on 2022-04-14 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_soluciones', '0057_solucion_slug_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemsolucionimagen',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='itemsolucionimagen',
            name='slug_en',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
