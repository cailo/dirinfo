# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name=b'fecha')),
                ('init', models.TimeField(null=True, verbose_name=b'hora de inicio', blank=True)),
                ('end', models.TimeField(null=True, verbose_name=b'hora de finalizaci\xc3\xb3n', blank=True)),
                ('matter', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['date'],
                'verbose_name': 'tarea',
                'verbose_name_plural': 'tareas',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.SlugField(unique=True)),
                ('text_color', models.CharField(default=b'#000000', max_length=7, verbose_name=b'color de texto')),
                ('background', models.CharField(default=b'#ffffff', max_length=7, verbose_name=b'color de fondo')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'tema',
                'verbose_name_plural': 'temas',
            },
        ),
        migrations.AddField(
            model_name='task',
            name='topic',
            field=models.ForeignKey(to='billboard.Topic'),
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
