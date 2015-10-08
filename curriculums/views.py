# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views import generic
from django.views.generic import (
    ListView, CreateView, DetailView, DeleteView, UpdateView
    )
#from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.views.generic.detail import DetailView
from .models import Data
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class DataList(ListView):
    """
    """
    model = Data
    template_name = 'curriculums/data_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DataList, self).dispatch(*args, **kwargs)

class DataCreate(CreateView):
    model = Data
    fields = ['name', 'title', 'area', 'teaching', 'curriculum', 'image']
    template_name = 'curriculums/data_form.html'
    success_url = reverse_lazy('curriculums:list')
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DataCreate, self).dispatch(*args, **kwargs)
    
    #def get_accountable(self, **kwargs):
    #       id = self.kwargs['pk']
    #       user = User.objects.get(id=id)
    #       return user     

    def clean_accountable(self):
        #data = self.cleaned_data['tourist']
        account = self.cleaned_data.get('accountable')
        try:
            profile = model.objects.get(owner=self.cleaned_data['accountable'])
        except model.DoesNotExist:
            return account
        raise forms.ValidationError("Usted ya tiene un curriculum cargado")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.accountable = self.request.user
        self.object.save()
        return super(DataCreate, self).form_valid(form)

        #if self.object.accountable != self:
        #    self.object.save()
        #    return super(DataCreate, self).form_valid(form)
        #else:
        #    raise forms.ValidationError("No hay cupo en la distancia seleccionada")  

        #if Data.objects.filter(related_field=self.get_accountable()):
        #    ctx = self.get_context_data(form=form)
        #    ctx['massive_error'] = True
        #    return self.render_to_response(ctx)
        #else:
        #    self.object.save()
        #    return super(DataCreate, self).form_valid(form)
    

class DataDetail(DetailView):
    """
    """
    model = Data
    template_name = 'curriculums/data_detail.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DataDetail, self).dispatch(*args, **kwargs)


class DataUpdate(UpdateView):
    model = Data
    template_name = 'curriculums/data_update_form.html'
    success_url = reverse_lazy('curriculums:list')
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DataUpdate, self).dispatch(*args, **kwargs)

    fields = ['name', 'title', 'area', 'teaching', 'curriculum', 'image']
    template_name_suffix = '_update_form'
    
    #def get_absolute_url(self):
    #    return reverse('curriculums.views.DataDetail', args=[self.pk])
 
    ##def get_success_url(self):
    ##    return reverse('curriculums.views.DataDetail', args=[self.pk])
        #return reverse('curriculums.views.DataDetail', args=[str(self.id)])

class DataDelete(DeleteView):
    """
    """
    model = Data

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DataDelete, self).dispatch(*args, **kwargs)

