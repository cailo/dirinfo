# -*- coding: utf-8 -*-

from django.conf.urls import url
from billboard.views import (TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView)

urlpatterns = [
    url(r'^$',
        TaskListView.as_view(),
        name='list'
        ),
    url(r'^create/$',
        TaskCreateView.as_view(),
        name='create'
        ),
    url(r'^(?P<pk>\d+)/update/$',
        TaskUpdateView.as_view(),
        name='update'
        ),
    url(r'^(?P<pk>\d+)/delete/$',
        TaskDeleteView.as_view(),
        name='delete'
        ),
]
