from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group, User

  
class ListAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'organization', 'car_brend', 'car_number', 'date_given', 'deadline', 'number_license', 'phone_number',)
    search_fields =['car_number', 'organization',]
    ordering = ('deadline',)

    
     
            
class PutyovkaAdmin(admin.ModelAdmin):
    raw_id_fields = ("car_number",)
    list_display= ('date', 'car_number', 'money',)
    search_fields =['car_number__car_number',]
                 
                 

 
admin.site.register(List, ListAdmin)    
admin.site.register(Putyovka, PutyovkaAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)

