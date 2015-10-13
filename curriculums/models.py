# -*- coding: utf-8 -*-

from django.db import models
#from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Data(models.Model):
    ''''''
    ''''''
    LOAD_CHOICES = (
        (1, 'Profesor Titular'),
        (2, 'Profesor Asocoado'),
        (3, 'Profesor Adjunto'),
	(4, 'Jefe de Trabajo Practicos'),
	(5, 'Auxiliar de 1era'),
        (6, 'Auxiliar de 2da')
    )

    CATEGORY_CHOICES = (
        (1, 'S/C'),
        (2, '1'),
        (3, '2'),
	(4, '3'),
	(5, '4'),
        (6, '5')
    )

    name = models.CharField('nombre completo', max_length=128)
    title = models.CharField('titulo', max_length=128)
    load = models.PositiveIntegerField('cargo', choices=LOAD_CHOICES)
    area = models.CharField('area de investigacion', max_length=128)
    matter = models.CharField('materia', max_length=100)
    category = models.PositiveIntegerField('categoria docente investigador', choices=CATEGORY_CHOICES)
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

