# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20160815_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='risk_type',
            field=models.CharField(default=b'i', max_length=3, verbose_name=b'Clisificacion de riesgo', choices=[(b'i', b'I'), (b'ii', b'IIa'), (b'iib', b'IIb'), (b'iii', b'III')]),
        ),
    ]
