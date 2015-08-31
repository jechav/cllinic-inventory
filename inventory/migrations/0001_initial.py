# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'fecha de creacion')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'fecha de modificacion')),
                ('model', models.CharField(max_length=255)),
                ('feature', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'fecha de creacion')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'fecha de modificacion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'fecha de creacion')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'fecha de modificacion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Manufacture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'fecha de creacion')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'fecha de modificacion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'fecha de creacion')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'fecha de modificacion')),
                ('model', models.CharField(max_length=255)),
                ('series', models.CharField(max_length=255)),
                ('voltage', models.IntegerField()),
                ('voltage_type', models.CharField(default=b'ac', max_length=2, choices=[(b'ac', b'AC'), (b'dc', b'DC')])),
                ('frequency', models.CharField(default=b'60', max_length=2, null=True, choices=[(b'60', b'60hz'), (b'50', b'50hz')])),
                ('property', models.CharField(default=b'ho', max_length=2, choices=[(b'ho', b'HOSPITAL'), (b'pr', b'PRESTADO'), (b'co', b'COMODATO'), (b'me', b'MEDICO')])),
                ('state', models.CharField(default=b'on', max_length=2, choices=[(b'on', b'OPERATIVO'), (b'of', b'DANADO')])),
                ('type', models.CharField(default=b'fx', max_length=2, choices=[(b'fx', b'FIJO'), (b'mv', b'MOVIL')])),
                ('accessories', models.ManyToManyField(to='inventory.Accessory')),
                ('brand', models.ForeignKey(to='inventory.Brand')),
                ('location', models.ForeignKey(to='inventory.Location')),
                ('manufacture', models.ForeignKey(to='inventory.Manufacture')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
