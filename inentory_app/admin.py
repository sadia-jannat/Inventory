from django.contrib import admin

# Register your models here.

from  .models import *

@admin.register(DeviceProuct)
class DeviceProuctAdmin(admin.ModelAdmin):
    list_display= ('brand','modelname','device_series','device_number','processor_brand','generation','processor_model','cpu_cache',
        'display_size', 'display_type', 'display_size', 'display_resolution', 'touch_screen', 'ram', 'ram_type', 'hdd', 'ssd', 'optical_drive',
        'keyboard_back_lit', 'finger_print_sensor', 'wifi', 'operating_system', 'weight', 'warranty')



@admin.register(TotalProduct)
class TotalProductAdmin(admin.ModelAdmin):
    list_display= ('device','stuff','lastdate')

    
@admin.register(InventoryLevel)
class InventoryLevelAdmin(admin.ModelAdmin):
    list_display= ('sales_summaries', 'stuff', 'stock_type', 'stock_range', 'sales_num', 'lastdate')    
