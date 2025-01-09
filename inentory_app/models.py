from django.db import models

# Create your models here.
BOOL=(
    ('Yes','Yes'),
    ('No','No'),
)

class DeviceProuct(models.Model):
    brand=models.CharField(max_length=100)
    modelname=models.CharField(max_length=200)
    device_series=models.CharField(max_length=200)
    device_number=models.IntegerField()
    processor_brand=models.CharField( max_length=50)
    generation=models.CharField(max_length=200)
    processor_model=models.CharField(max_length=50)
    cpu_cache=models.CharField(max_length=50)
    display_size=models.FloatField()
    display_type=models.CharField(max_length=100)
    display_resolution=models.CharField(max_length=100)
    touch_screen=models.CharField(choices=BOOL, max_length=50)
    ram=models.CharField(max_length=100)
    ram_type=models.CharField(max_length=100)
    hdd=models.CharField(max_length=100)
    ssd=models.CharField(max_length=100)
    optical_drive=models.CharField(choices=BOOL, max_length=50)
    keyboard_back_lit=models.CharField(choices=BOOL, max_length=50)
    finger_print_sensor=models.CharField(choices=BOOL, max_length=50)
    wifi=models.CharField(max_length=100)
    operating_system=models.CharField(max_length=100)
    weight=models.FloatField()
    warranty=models.CharField(max_length=100)


   
    class Meta:
        verbose_name = "brand"
        verbose_name_plural = "brand" 


class TotalProduct(models.Model):
    device=models.OneToOneField(DeviceProuct, on_delete=models.CASCADE)
    stuff=models.CharField(max_length=100)
    lastdate=models.DateField()


class InventoryLevel(models.Model):
    sales_summaries=models.CharField(max_length=200)
    stuff=models.CharField(max_length=100)
    stock_type=models.CharField(max_length=100)
    stock_range=models.IntegerField()
    sales_num=models.IntegerField()
    lastdate=models.DateField()

    
        