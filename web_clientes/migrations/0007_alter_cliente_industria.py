# Generated by Django 3.2.12 on 2022-04-07 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_clientes', '0006_auto_20220406_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='industria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='clientes', to='web_clientes.clienteindustria'),
        ),
    ]
