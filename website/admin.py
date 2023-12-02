from django.contrib import admin
from website.models import Contact,Newsletter


 
class ContactAdmin (admin.ModelAdmin):
     date_hierarchy = "created_date"
     empty_value_display = "-empty-"
     list_display = ['name','email', 'created_date']  
     search_fields = ['name','message']
     list_filter=['email']
 
     class Meta:
         ordering=('created_date' )
        
admin.site.register(Contact,ContactAdmin)    
admin.site.register(Newsletter)