# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    name = models.CharField(max_length=100)
    code = models.SlugField(max_length=50, unique=True)
    text_color = models.CharField('color de texto', max_length=7, default='#000000')
    background = models.CharField('color de fondo', max_length=7, default='#ffffff')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tema'
        verbose_name_plural = 'temas'
        ordering = ['name']

class Task(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField('fecha')
    init = models.TimeField('hora de inicio', blank=True, null=True)
    end = models.TimeField('hora de finalización', blank=True, null=True)
    topic = models.ForeignKey(Topic)
    matter = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.matter

    def get_time(self):
        if self.init and self.end:
            return u'de %s hasta %s' % (self.init, self.end)

    class Meta:
        verbose_name = 'tarea'
        verbose_name_plural = 'tareas'
        ordering = ['date']
