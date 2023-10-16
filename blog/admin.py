from django.contrib import admin
from blog.models import post 

class postAdmin(admin.ModelAdmin):
    list_display=['title','counted_views','status','published_date','created_date']
    list_filter=('status',)
    search_fields=['title','content']
    empty_value_display = '-empty-'
    date_hierarchy ='created_date'
    
admin.site.register(post,postAdmin)