# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20150902_0831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='voltage',
        ),
        migrations.AddField(
            model_name='product',
            name='calibration',
            field=models.BooleanField(default=False, verbose_name=b'Calibracion'),
        ),
        migrations.AddField(
            model_name='product',
            name='capacity',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Capacidad'),
        ),
        migrations.AddField(
            model_name='product',
            name='characteristics',
            field=models.TextField(null=True, verbose_name=b'Caracteristicas'),
        ),
        migrations.AddField(
            model_name='product',
            name='city',
            field=models.CharField(default=b'MAGANGE', max_length=255, verbose_name=b'City'),
        ),
        migrations.AddField(
            model_name='product',
            name='clinic',
            field=models.CharField(default=b'HOSPITAL DIVINA MISERICORDIA', max_length=255, verbose_name=b'Clinica'),
        ),
        migrations.AddField(
            model_name='product',
            name='code',
            field=models.CharField(default=datetime.datetime(2016, 8, 15, 17, 15, 11, 180956, tzinfo=utc), max_length=255, serialize=False, verbose_name=b'Codigo', primary_key=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='condition',
            field=models.CharField(default=b'OPTIMO', max_length=2, verbose_name=b'Condicion Operativa', choices=[(b'1', b'OPTIMO'), (b'2', b'BUENO'), (b'3', b'REGULAR'), (b'4', b'MALO'), (b'5', b'OBSOLETO')]),
        ),
        migrations.AddField(
            model_name='product',
            name='consumption',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Consumo'),
        ),
        migrations.AddField(
            model_name='product',
            name='cost',
            field=models.DecimalField(null=True, verbose_name=b'Costo', max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='product',
            name='date_purchase',
            field=models.DateField(null=True, verbose_name=b'Fecha de Compra'),
        ),
        migrations.AddField(
            model_name='product',
            name='department',
            field=models.CharField(default=b'BOLIVAR', max_length=255, verbose_name=b'Departamento'),
        ),
        migrations.AddField(
            model_name='product',
            name='electric',
            field=models.BooleanField(default=False, verbose_name=b'Electrico'),
        ),
        migrations.AddField(
            model_name='product',
            name='electromagnetic',
            field=models.BooleanField(default=False, verbose_name=b'Electromagnetico'),
        ),
        migrations.AddField(
            model_name='product',
            name='electronic',
            field=models.BooleanField(default=False, verbose_name=b'Electronico'),
        ),
        migrations.AddField(
            model_name='product',
            name='floor',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Piso'),
        ),
        migrations.AddField(
            model_name='product',
            name='hydraulic',
            field=models.BooleanField(default=False, verbose_name=b'Hidraulico'),
        ),
        migrations.AddField(
            model_name='product',
            name='invima',
            field=models.CharField(default=datetime.datetime(2016, 8, 15, 17, 15, 32, 268982, tzinfo=utc), max_length=255, verbose_name=b'Invima'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='maintenance_protocol',
            field=models.BooleanField(default=False, verbose_name=b'Protocolo de mantenimiento'),
        ),
        migrations.AddField(
            model_name='product',
            name='mechanic',
            field=models.BooleanField(default=False, verbose_name=b'Mecanico'),
        ),
        migrations.AddField(
            model_name='product',
            name='n_inventary',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Numero de inventario'),
        ),
        migrations.AddField(
            model_name='product',
            name='other',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Otro'),
        ),
        migrations.AddField(
            model_name='product',
            name='p_calibration',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Periodo de Calibracion'),
        ),
        migrations.AddField(
            model_name='product',
            name='p_maintenance',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Periodicidad de Mantenimiento'),
        ),
        migrations.AddField(
            model_name='product',
            name='phisycal_location',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Localizacion Fisica'),
        ),
        migrations.AddField(
            model_name='product',
            name='power',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Potencia'),
        ),
        migrations.AddField(
            model_name='product',
            name='pressure',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Presion'),
        ),
        migrations.AddField(
            model_name='product',
            name='region',
            field=models.CharField(default=b'CARIBE', max_length=255, verbose_name=b'Region'),
        ),
        migrations.AddField(
            model_name='product',
            name='risk_type',
            field=models.CharField(default=b'i', max_length=3, verbose_name=b'Clisificacion de riesgo', choices=[(b'i', b'I'), (b'ii', b'II'), (b'iii', b'III'), (b'iv', b'IV'), (b'v', b'V')]),
        ),
        migrations.AddField(
            model_name='product',
            name='service_manual',
            field=models.BooleanField(default=False, verbose_name=b'Manual de Servicio'),
        ),
        migrations.AddField(
            model_name='product',
            name='steam',
            field=models.BooleanField(default=False, verbose_name=b'Vapor'),
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Proveedor'),
        ),
        migrations.AddField(
            model_name='product',
            name='temperature',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Temperatura'),
        ),
        migrations.AddField(
            model_name='product',
            name='tire',
            field=models.BooleanField(default=False, verbose_name=b'neumatico'),
        ),
        migrations.AddField(
            model_name='product',
            name='tower',
            field=models.CharField(default=b'N/A', max_length=255, verbose_name=b'Torre'),
        ),
        migrations.AddField(
            model_name='product',
            name='warranty',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Garantia'),
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Peso'),
        ),
        migrations.AlterField(
            model_name='product',
            name='state',
            field=models.CharField(default=b'OPTIMO', max_length=2, verbose_name=b'Estado Funcionamiento', choices=[(b'1', b'OPTIMO'), (b'2', b'BUENO'), (b'3', b'REGULAR'), (b'4', b'MALO'), (b'5', b'OBSOLETO')]),
        ),
    ]
