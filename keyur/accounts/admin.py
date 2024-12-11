from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.CustomerDetails)
class CustomerDetailsAdmin(admin.ModelAdmin):
    list_display = ['studio_name','full_name','mobile','address','state','city','pincode']


@admin.register(models.Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['user','date','delivery_date','product_name','make','model','serial_number','customer_issues','collected_accessories','service_charge','parts_charge']
