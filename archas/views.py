import os
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import *
from .forms import InteractionForm

from django.urls import reverse, reverse_lazy
from django.core import serializers

from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView

import requests
import json, xmljson
from lxml.etree import fromstring, tostring


class AutomatedSystemListView(ListView):
    model = AutomatedSystem
    template_name = 'archas/archas_category_view.html'
    context_object_name = 'automated_system_list'
    
class AutomatedSystemDetailView(DetailView):
    model = AutomatedSystem
    slug_field = 'id'
    template_name = 'archas/archas_as_view.html'
    context_object_name = 'automated_system'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['interactions_list'] = Interaction.objects.filter(automated_system=self.object)
        return context

class AutomatedSystemUpdate(UpdateView):
    model = AutomatedSystem
    slug_field = 'id'
    template_name = 'archas/as_update.html'
    fields = ['code','name','owner','status','cloud_ready','platform_ready','owner_block','owner_tribe','full_name','nickname',
    'short_description','rsa_id','service_desk_id','guid','centralization_level','system_criticality','target_status','target_readiness','as_lider',
    'as_architect','architect_in_charge','editors',]
    def get_success_url(self):
        return reverse_lazy('archas:as_detail', kwargs={'slug': getattr(self.object,'id')})

class TargetArchitectureUpdate(UpdateView):
    model = AutomatedSystem
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = 'archas/as_ta_update.html'
    fields = ['target_architecture_diagram']
    def get_success_url(self):
        return reverse_lazy('archas:as_detail', kwargs={'slug': getattr(self.object,'id')})
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['automated_system'] = self.object
        return context

class InteractionsListUpdate(ListView):
    model = Interaction
    template_name = 'archas/as_intlist_update.html'
    context_object_name = 'interactions_list'
    def get_queryset(self):
        self.automated_system = get_object_or_404(AutomatedSystem, id=self.kwargs['automated_system_id'])
        return Interaction.objects.filter(automated_system=self.automated_system)
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['automated_system'] = get_object_or_404(AutomatedSystem, id=self.kwargs['automated_system_id'])
        return context



class InteractionUpdate(UpdateView):
    model = Interaction
    slug_field = 'id'
    slug_url_kwarg = 'interaction_id'
    template_name = 'archas/interaction_update.html'
    def get_success_url(self):
        automated_system_id = Interaction.objects.get(pk=self.kwargs['interaction_id']).automated_system.id
        return reverse_lazy('archas:int_list_update', kwargs={'automated_system_id': automated_system_id})
    fields = [
            'code',
            'int_type',
            'protocol', 
            'as_provider',
            'fp_provider',
            'description',
            'status',
            'iniciator',
            'int_technology',
            'consumer_status',
            'consumer_date',
            'consumer_as',
            'consumer_role',
            'consumer_process',
            'consumer_sla',
            'consumer_comment',
            'data_description',
            'data_encoding',
            'data_format',
            'data_confidential_level',
            'data_integrity_level',
            'schedule_initiation',
            'schedule_year',
            'schedule_month',
            'schedule_week',
            'schedule_day',
            'schedule_load_profile',
            'filesize_min',
            'filesize_max',
            'filesize_avg',
            'security_ssl_tls',
            'security_encription',
            'security_digital_signature',
            'architecture_standard_complience',
            'int_comment']


class InteractionCreate(CreateView):
    model = Interaction
    template_name = 'archas/interaction_update.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['automated_system'] = get_object_or_404(AutomatedSystem, id=self.kwargs['automated_system_id'])
        return context
    def form_valid(self, form):
        form.instance.automated_system = get_object_or_404(AutomatedSystem, id=self.kwargs['automated_system_id'])
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('archas:int_list_update', kwargs={'automated_system_id': self.kwargs['automated_system_id']})
    fields = [
            'code',
            'int_type',
            'protocol', 
            'as_provider',
            'fp_provider',
            'description',
            'status',
            'iniciator',
            'int_technology',
            'consumer_status',
            'consumer_date',
            'consumer_as',
            'consumer_role',
            'consumer_process',
            'consumer_sla',
            'consumer_comment',
            'data_description',
            'data_encoding',
            'data_format',
            'data_confidential_level',
            'data_integrity_level',
            'schedule_initiation',
            'schedule_year',
            'schedule_month',
            'schedule_week',
            'schedule_day',
            'schedule_load_profile',
            'filesize_min',
            'filesize_max',
            'filesize_avg',
            'security_ssl_tls',
            'security_encription',
            'security_digital_signature',
            'architecture_standard_complience',
            'int_comment']
            

def interaction_remove(request, interaction_id):
    interaction = Interaction.objects.get(pk=interaction_id)
    automated_system = interaction.automated_system
    interaction.delete()
    return HttpResponseRedirect(reverse('archas:int_list_update',kwargs={'automated_system_id':automated_system.id}))



def index(request):
    return render(request, 'archas/archas_category_view.html')
    # as_list = AutomatedSystem.objects.all()
    # int_list = Interaction.objects.all()
    # context = {'as_list': as_list, 'int_list': int_list, 'as_id': 1}
    # return render(request, 'archas/index.html', context)

def as_detail(request, as_id):
    return HttpResponse("Some AS details with id %s")

def add_int(request, as_id):
    if request.method == 'POST':
        form = InteractionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('archas:index'))
    else:
        form = InteractionForm()
    return render(request, 'archas/add_int_form.html', {'as_id': as_id, 'form':form})


def edit_int(request, int_id):
    if request.method == 'POST':
        form = InteractionForm(request.POST)
        if form.is_valid():
            interaction = Interaction.objects.get(pk=int_id)
            form = InteractionForm(request.POST, instance=interaction)
            form.save()
            return HttpResponseRedirect(reverse('archas:index'))
    else:
        interaction = Interaction.objects.get(pk=int_id)
        form = InteractionForm(instance=interaction)
    return render(request, 'archas/edit_int_form.html', {'int_id':int_id, 'form':form})

def upload_json(*args):
    data = serializers.serialize("json", Interaction.objects.all())
    response = HttpResponse(charset='UTF-8',content_type='application/force-download', content=str(data))
    response['Content-Disposition'] = 'attachment; filename=' + os.path.basename('as_inetractions.json')
    return response

def arachas_base(request, *args):
    return render(request, 'archas/archas_base.html')

def as_view(request, *args):
    return render(request, 'archas/archas_as_view.html')

def category_view(request, *args):
    return render(request, 'archas/archas_category_view.html')

def confluence(request, *args):

    pageId = request.GET.get('pageId', '753677')

    r = requests.get('http://130.193.36.149:8090/rest/api/content/'+str(pageId)+'?expand=body.storage', auth=('admin', 'adminadmin'))
    page_title = r.json()['title']
    page_body_xml = r.json()['body']['storage']['value']

    xml = fromstring('<page>'+page_body_xml+'</page>')
    page_body_parsed_json = json.dumps(xmljson.parker.data(xml))

    page_body_minidom_json = json.loads(page_body_parsed_json)
    page_body_pretty_json = json.dumps(page_body_minidom_json, indent=4)

    json_pretty = '{"json":"good"}'
    context = {'page_title': page_title, 'page_body_json': page_body_pretty_json}

    return render (request, 'archas/confluence.html', context)

class AboutView(TemplateView):
    template_name = "archas/archas_category_view.html"

class BookListView(ListView):
    model = Interaction
    template_name = 'archas/index.html'
    context_object_name = 'int_list'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        # context['book_list'] = Book.objects.all()
        context['as_id'] = 1
        return context

