# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20150902_0736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sublocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Nombre')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'fecha de creacion')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'fecha de modificacion')),
            ],
            options={
                'verbose_name': 'Localizacion',
                'verbose_name_plural': 'Localizaciones',
            },
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'Servicio', 'verbose_name_plural': 'Servicio'},
        ),
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.ForeignKey(verbose_name=b'Localizacion', to='inventory.Sublocation'),
        ),
        migrations.AddField(
            model_name='sublocation',
            name='service',
            field=models.ForeignKey(verbose_name=b'Servicio', to='inventory.Location'),
        ),
    ]
