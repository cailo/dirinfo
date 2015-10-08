# -*- coding: utf-8 -*-

from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=128)
    date_init = models.DateField('fecha de inicio')
    date_end = models.DateField('fecha de finalización')
    init = models.TimeField('hora de inicio', blank=True, null=True)
    end = models.TimeField('hora de finalización', blank=True, null=True)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_date_init(self):
        return u'de %s hasta %s' % (self.date_init, self.init)

    def get_date_end(self):
        return u'de %s hasta %s' % (self.date_end, self.end)

    class Meta:
        verbose_name = 'evento'
        verbose_name_plural = 'eventos'
        ordering = ['date_init']

class Activity(models.Model):
    event = models.ForeignKey(Event)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    date_init = models.DateField('fecha de inicio')
    date_end = models.DateField('fecha de finalización')
    init = models.TimeField('hora de inicio', blank=True, null=True)
    end = models.TimeField('hora de finalización', blank=True, null=True)
    description = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    maps_lat = models.IntegerField()
    maps_lng = models.IntegerField()

    def __str__(self):
        return self.title
        #return u'%s   %s' % (self.date_init, self.init)

    def get_coordinates(self):
        return u'%s,%s' % (self.maps_lat, self.maps_lng)

    class Meta:
        verbose_name = 'actividad'
        verbose_name_plural = 'actividades'
        ordering = ['title']
