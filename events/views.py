# -*- coding: utf-8 -*-

from django.views.generic import (CreateView, ListView, UpdateView, DeleteView)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from events.models import Event, Activity


class EventListView(ListView):
    model = Event

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventListView, self).dispatch(*args, **kwargs)

    #def get_queryset(self):
    #    return Event.objects.filter(user=self.request.user)


class EventCreateView(CreateView):
    model = Event
    fields = ['name', 'date_init', 'date_end', 'init', 'end', 'description']
    success_url = reverse_lazy('events:list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EventCreateView, self).form_valid(form)


class EventUpdateView(UpdateView):
    model = Event
    fields = ['name', 'date_init', 'date_end', 'init', 'end', 'description']
    success_url = reverse_lazy('events:list')
    template_name_suffix = '_update_form'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EventUpdateView, self).form_valid(form)


class EventDeleteView(DeleteView):
    model = Event
    success_url = reverse_lazy('events:list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventDeleteView, self).dispatch(*args, **kwargs)


class ActivityListView(ListView):
    model = Activity

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ActivityListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Activity.objects.filter(event=self)


class ActivityCreateView(CreateView):
    model = Activity
    fields = ['title', 'subtitle', 'date_init', 'date_end', 'init', 'end', 'description', 'address', 'maps_lat', 'maps_lng']
    success_url = reverse_lazy('events:list_activity')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ActivityCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ActivityCreateView, self).form_valid(form)


class ActivityUpdateView(UpdateView):
    model = Activity
    fields = ['title', 'subtitle', 'date_init', 'date_end', 'init', 'end', 'description', 'address', 'maps_lat', 'maps_lng']
    success_url = reverse_lazy('events:list_activity')
    template_name_suffix = '_update_form'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ActivityUpdateView, self).form_valid(form)


class ActivityDeleteView(DeleteView):
    model = Activity
    success_url = reverse_lazy('events:list_activity')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ActivityDeleteView, self).dispatch(*args, **kwargs)
