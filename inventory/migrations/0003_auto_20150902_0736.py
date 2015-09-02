# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20150902_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='accessories',
            field=models.ManyToManyField(to='inventory.Accessory', verbose_name=b'Accesorios', blank=True),
        ),
    ]
