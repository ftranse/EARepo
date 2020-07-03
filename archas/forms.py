from django.forms import ModelForm
from django import forms
from .models import Interaction

class NameForm(forms.Form):
        your_name = forms.CharField(label='Your name', max_length=100)

class InteractionForm(ModelForm):
    class Meta:
        model = Interaction
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