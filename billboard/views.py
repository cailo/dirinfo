# -*- coding: utf-8 -*-

from django.views.generic import (CreateView, ListView, UpdateView, DeleteView)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from billboard.models import Task


class TaskListView(ListView):
    model = Task

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskCreateView(CreateView):
    model = Task
    fields = ['date', 'init', 'end', 'topic', 'matter', 'description']
    success_url = reverse_lazy('billboard:list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['date', 'topic', 'matter', 'description']
    success_url = reverse_lazy('billboard:list')
    template_name_suffix = '_update_form'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskUpdateView, self).form_valid(form)


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('billboard:list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskDeleteView, self).dispatch(*args, **kwargs)
