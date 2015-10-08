# -*- coding: utf-8 -*-

from django.contrib import admin
from billboard.models import Topic, Task

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
