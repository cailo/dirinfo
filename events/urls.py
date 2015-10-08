# -*- coding: utf-8 -*-

from django.conf.urls import url
from events.views import (
    EventListView, EventCreateView, EventUpdateView, EventDeleteView, ActivityListView, ActivityCreateView, ActivityUpdateView, ActivityDeleteView
    )

urlpatterns = [
    url(r'^$', EventListView.as_view(), name='list'),
    url(r'^create/$', EventCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/update/$', EventUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', EventDeleteView.as_view(), name='delete'),
    url(r'^activity/(?P<pk>\d+)/$', ActivityListView.as_view(), name='list_activity'),
    url(r'^activity/create/(?P<pk>\d+)/$', ActivityCreateView.as_view(), name='create_activity'),
    url(r'^activity/update/(?P<pk>\d+)/$', ActivityUpdateView.as_view(), name='update_activity'),
    url(r'^activity/delete/(?P<pk>\d+)/$', ActivityDeleteView.as_view(), name='delete_activity'),
    #url(r'^(?P<pk>\d+)/activity/(?A<pk>\d+)/$', ActivityListView.as_view(), name='list_activity'),
    #url(r'^(?P<pk>\d+)/activity/(?A<pk>\d+)/create/$', ActivityCreateView.as_view(), name='create_activity'),
    #url(r'^(?P<pk>\d+)/activity/(?A<pk>\d+)/update/$', ActivityUpdateView.as_view(), name='update_activity'),
    #url(r'^(?P<pk>\d+)/activity/(?A<pk>\d+)/delete/$', ActivityDeleteView.as_view(), name='delete_activity'),
]
