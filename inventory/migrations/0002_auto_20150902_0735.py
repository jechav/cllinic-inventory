# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accessory',
            options={'verbose_name': 'Accesorio', 'verbose_name_plural': 'Accesorios'},
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'Marca', 'verbose_name_plural': 'Marcas'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'Localizacion', 'verbose_name_plural': 'Localizaciones'},
        ),
        migrations.AlterModelOptions(
            name='manufacture',
            options={'verbose_name': 'Fabricante', 'verbose_name_plural': 'Frabricantes'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Equipo', 'verbose_name_plural': 'Equipos'},
        ),
        migrations.AlterField(
            model_name='accessory',
            name='feature',
            field=models.CharField(max_length=255, verbose_name=b'Caracteristicas'),
        ),
        migrations.AlterField(
            model_name='accessory',
            name='model',
            field=models.CharField(max_length=255, verbose_name=b'Modelo'),
        ),
        migrations.AlterField(
            model_name='accessory',
            name='name',
            field=models.CharField(max_length=255, verbose_name=b'Nombre'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=255, verbose_name=b'Nombre'),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=255, verbose_name=b'Nombre'),
        ),
        migrations.AlterField(
            model_name='manufacture',
            name='name',
            field=models.CharField(max_length=255, verbose_name=b'Nombre'),
        ),
        migrations.AlterField(
            model_name='product',
            name='accessories',
            field=models.ManyToManyField(to='inventory.Accessory', null=True, verbose_name=b'Accesorios'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(verbose_name=b'Marca', to='inventory.Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='frequency',
            field=models.CharField(default=b'60', max_length=2, null=True, verbose_name=b'Frecuencia', choices=[(b'60', b'60hz'), (b'50', b'50hz')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.ForeignKey(verbose_name=b'Localizacion', to='inventory.Location'),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacture',
            field=models.ForeignKey(verbose_name=b'Fabricante', to='inventory.Manufacture'),
        ),
        migrations.AlterField(
            model_name='product',
            name='model',
            field=models.CharField(max_length=255, verbose_name=b'Modelo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name=b'Nombre'),
        ),
        migrations.AlterField(
            model_name='product',
            name='property',
            field=models.CharField(default=b'ho', max_length=2, verbose_name=b'Propietario', choices=[(b'ho', b'HOSPITAL'), (b'pr', b'PRESTADO'), (b'co', b'COMODATO'), (b'me', b'MEDICO')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='series',
            field=models.CharField(max_length=255, verbose_name=b'Serie'),
        ),
        migrations.AlterField(
            model_name='product',
            name='state',
            field=models.CharField(default=b'on', max_length=2, verbose_name=b'Estado', choices=[(b'on', b'OPERATIVO'), (b'of', b'DANADO')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(default=b'fx', max_length=2, verbose_name=b'Tipo', choices=[(b'fx', b'FIJO'), (b'mv', b'MOVIL')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='voltage',
            field=models.IntegerField(verbose_name=b'Voltaje'),
        ),
        migrations.AlterField(
            model_name='product',
            name='voltage_type',
            field=models.CharField(default=b'ac', max_length=2, verbose_name=b'Tipo de Voltaje', choices=[(b'ac', b'AC'), (b'dc', b'DC')]),
        ),
    ]
