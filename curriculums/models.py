# -*- coding: utf-8 -*-

from django.db import models
#from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Data(models.Model):
    name = models.CharField('nombre completo', max_length=128)
    title = models.CharField('titulo', max_length=128)
    area = models.CharField('area de investigacion', max_length=128)
    teaching = models.CharField('docencia', max_length=100)
    curriculum = models.FileField('curriculum', upload_to='curriculums', null=True, blank=True)
    image = models.ImageField('imagen', upload_to='images')
    accountable = models.OneToOneField(User)

    #def get_absolute_url(self):
    #    return reverse('detail', args=[str(self.id)])
    
    def get_absolute_url(self):
        return "/curriculums/%i/" % self.id

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Curriculums Docente'
        verbose_name_plural = 'Curriculums Docentes'

