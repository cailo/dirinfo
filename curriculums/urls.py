# -*- coding: utf-8 -*-

from django.conf.urls import url
#from events.views import (
#    EventListView, EventCreateView, EventUpdateView, EventDeleteView
#    )
from curriculums.views import DataCreate, DataDetail, DataUpdate, DataList

urlpatterns = [
    url(r'^datos/', DataCreate.as_view(), name='datos'),
    url(r'^detail/(?P<pk>\d+)$', DataDetail.as_view(), name='detail'),
    url(r'^update/(?P<pk>\d+)$', DataUpdate.as_view(), name='update_data'),
    url(r'^$', DataList.as_view(), name='list'),
]
