from django.shortcuts import render,get_object_or_404
from blog.models import post
from django.utils import timezone
 

def blog_view(request,cat_name=None):
   
    posts= post.objects.filter(published_date__lte=timezone.now(),status=1)
    if cat_name:
        posts=posts.filter(category__name=cat_name)
    context={'posts':posts} 
    return render (request,'blog/blog-home.html',context)
      
              
def blog_single(request,pid):

    posts=get_object_or_404(post,pk=pid,status=1,published_date__lte=timezone.now())
    if post:
        posts.counted_views = posts.counted_views + 1
        posts.save()
        
    related_posts= post.objects.filter(published_date__lte=timezone.now(),status=1)
    nextp= related_posts.filter(id__gt=posts.id).order_by('id').first()
    previous=related_posts.filter(id__lt=posts.id).order_by('id').last()          
    context={'posts':posts ,'nextp': nextp ,'previous': previous }   
    return render (request,'blog/blog-single.html',context)

def blog_category(request,cat_name):
       
    posts= post.objects.filter(status=1)
    posts= posts.filter(category__name=cat_name)
    context={'posts':posts} 
    return render (request,'blog/blog-home.html',context)
       

   
def test (request):
    return render (request,'test.html')


                    


