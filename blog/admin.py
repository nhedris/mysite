from django.contrib import admin
from blog.models import post,category,Comment
from django_summernote.admin import SummernoteModelAdmin


class postAdmin(SummernoteModelAdmin):
    list_display=['title','author','counted_views','status','published_date','created_date']
    list_filter=('status','author',)
    search_fields=['title','content']
    summernote_fields = ('content',)
    empty_value_display = '-empty-'
    date_hierarchy ='created_date'
    
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy ='created_date'
    empty_value_display = '-empty-'
    list_display=['name','post','approved','created_date']
    list_filter=('post','approved',)
    search_fields=['name','post']
    

admin.site.register(Comment,CommentAdmin)    
admin.site.register(post,postAdmin)
admin.site.register(category)

