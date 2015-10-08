# -*- coding: utf-8 -*-

from django.contrib import admin
from concourses.models import Area, Professor, Result, ProfessorResult

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    pass

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_filter = ('area',)
    list_display = ('get_name', 'area',)

    def get_name(self, obj):
        return obj.user.get_full_name()

class ProfessorResultInline(admin.TabularInline):
    model = ProfessorResult

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    inlines = [ProfessorResultInline]
