# -*- coding: utf-8 -*-

from django.contrib import admin
from events.models import Event, Activity

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    pass

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
