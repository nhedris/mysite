from django import template
from blog.models import post
from blog.models import category

register = template.Library()

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

@register.inclusion_tag('blog/blog-post-category.html')
def postcategories():
    posts=post.objects.filter(status=1)
    categories=category.objects.all()
    cat_dict={}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories': cat_dict }    