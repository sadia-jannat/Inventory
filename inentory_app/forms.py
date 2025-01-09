import django
from django.contrib.auth import models
from django.core import validators
from django import forms
from django.forms import fields, widgets
from django import forms

#django form create kore bellow models and forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


#models
from .models import *


class Create(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2' ]


class DeviceProuctForm(forms.ModelForm):
    class Meta:
        model=DeviceProuct
        fields=['brand','modelname','device_series','device_number','processor_brand','generation','processor_model','cpu_cache',
        'display_size', 'display_type', 'display_size', 'display_resolution', 'touch_screen', 'ram', 'ram_type', 'hdd', 'ssd', 'optical_drive',
        'keyboard_back_lit', 'finger_print_sensor', 'wifi', 'operating_system', 'weight', 'warranty']


class InventoryLevelForm(forms.ModelForm):
    class Meta:
        model=InventoryLevel
        fields=['sales_summaries', 'stuff', 'stock_type', 'stock_range', 'sales_num', 'lastdate']



