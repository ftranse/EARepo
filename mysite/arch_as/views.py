import os
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import AutomatedSystem, Interaction
from .forms import InteractionForm

from django.urls import reverse
from django.core import serializers

def index(request):
    return render(request, 'arch_as/archas_category_view.html')
    # as_list = AutomatedSystem.objects.all()
    # int_list = Interaction.objects.all()
    # context = {'as_list': as_list, 'int_list': int_list, 'as_id': 1}
    # return render(request, 'arch_as/index.html', context)

def as_detail(request, as_id):
    return HttpResponse("Some AS details with id %s")

def add_int(request, as_id):
    if request.method == 'POST':
        form = InteractionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('arch_as:index'))
    else:
        form = InteractionForm()
    return render(request, 'arch_as/add_int_form.html', {'as_id': as_id, 'form':form})
            
def remove_int(request, int_id):
    Interaction.objects.get(pk=int_id).delete()
    return HttpResponseRedirect(reverse('arch_as:index'))

def edit_int(request, int_id):
    if request.method == 'POST':
        form = InteractionForm(request.POST)
        if form.is_valid():
            interaction = Interaction.objects.get(pk=int_id)
            form = InteractionForm(request.POST, instance=interaction)
            form.save()
            return HttpResponseRedirect(reverse('arch_as:index'))
    else:
        interaction = Interaction.objects.get(pk=int_id)
        form = InteractionForm(instance=interaction)
    return render(request, 'arch_as/edit_int_form.html', {'int_id':int_id, 'form':form})

def upload_json(*args):
    data = serializers.serialize("json", Interaction.objects.all())
    response = HttpResponse(charset='UTF-8',content_type='application/force-download', content=str(data))
    response['Content-Disposition'] = 'attachment; filename=' + os.path.basename('as_inetractions.json')
    return response

def arachas_base(request, *args):
    return render(request, 'arch_as/archas_base.html')

def as_view(request, *args):
    return render(request, 'arch_as/archas_as_view.html')

def category_view(request, *args):
    return render(request, 'arch_as/archas_category_view.html')