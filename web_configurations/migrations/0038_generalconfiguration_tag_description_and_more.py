# Generated by Django 4.0.4 on 2022-04-14 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_configurations', '0037_auto_20220407_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalconfiguration',
            name='tag_description',
            field=models.TextField(blank=True, max_length=160, null=True),
        ),
        migrations.AddField(
            model_name='generalconfiguration',
            name='tag_description_en',
            field=models.TextField(blank=True, max_length=160, null=True),
        ),
    ]