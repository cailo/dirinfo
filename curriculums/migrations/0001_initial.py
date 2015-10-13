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
            name='Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name=b'nombre completo')),
                ('title', models.CharField(max_length=128, verbose_name=b'titulo')),
                ('load', models.PositiveIntegerField(verbose_name=b'cargo', choices=[(1, b'Profesor Titular'), (2, b'Profesor Asocoado'), (3, b'Profesor Adjunto'), (4, b'Jefe de Trabajo Practicos'), (5, b'Auxiliar de 1era'), (6, b'Auxiliar de 2da')])),
                ('area', models.CharField(max_length=128, verbose_name=b'area de investigacion')),
                ('matter', models.CharField(max_length=100, verbose_name=b'materia')),
                ('category', models.PositiveIntegerField(verbose_name=b'categoria docente investigador', choices=[(1, b'S/C'), (2, b'1'), (3, b'2'), (4, b'3'), (5, b'4'), (6, b'5')])),
                ('curriculum', models.FileField(upload_to=b'curriculums', null=True, verbose_name=b'curriculum', blank=True)),
                ('image', models.ImageField(upload_to=b'images', verbose_name=b'imagen')),
                ('accountable', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Curriculums Docente',
                'verbose_name_plural': 'Curriculums Docentes',
            },
        ),
    ]
