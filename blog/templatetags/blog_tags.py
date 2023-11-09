from django import template

register = template.Library()
from blog.models import post


@register.simple_tag(name='posts')
def function():
    posts=post.objects.filter(status=1)
    return posts

@register.filter 
def snippet(value):
    return value[:5] + '...'
 
@register.inclusion_tag('blog/blog-popular-post.html')
def latesposts():
    posts=post.objects.filter(status=1).order_by('published_date')
    return {'posts' : posts} 
