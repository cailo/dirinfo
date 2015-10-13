# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=b'images', verbose_name=b'imagen')),
                ('date_init', models.DateField(verbose_name=b'fecha de inicio')),
                ('date_end', models.DateField(verbose_name=b'fecha de finalizaci\xc3\xb3n')),
                ('init', models.TimeField(null=True, verbose_name=b'hora de inicio', blank=True)),
                ('end', models.TimeField(null=True, verbose_name=b'hora de finalizaci\xc3\xb3n', blank=True)),
                ('description', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('linkinfo', models.CharField(max_length=512)),
                ('maps_lat', models.IntegerField()),
                ('maps_lng', models.IntegerField()),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'actividad',
                'verbose_name_plural': 'actividades',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('logo', models.ImageField(upload_to=b'images', verbose_name=b'logo')),
                ('date_init', models.DateField(verbose_name=b'fecha de inicio')),
                ('date_end', models.DateField(verbose_name=b'fecha de finalizaci\xc3\xb3n')),
                ('init', models.TimeField(null=True, verbose_name=b'hora de inicio', blank=True)),
                ('end', models.TimeField(null=True, verbose_name=b'hora de finalizaci\xc3\xb3n', blank=True)),
                ('description', models.CharField(max_length=256)),
            ],
            options={
                'ordering': ['date_init'],
                'verbose_name': 'evento',
                'verbose_name_plural': 'eventos',
            },
        ),
        migrations.AddField(
            model_name='activity',
            name='event',
            field=models.ForeignKey(to='events.Event'),
        ),
    ]
