from django import template
from django.db import models
from blog import models
from blog.models import post

register = template.Library()
 
@register.inclusion_tag('website/website-post.html')
def latesposts():
    posts=post.objects.filter(status=1).order_by('published_date')
    
    return { 'posts': posts } 
