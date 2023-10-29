from django.shortcuts import render,get_object_or_404
from blog.models import post
import datetime



def blog_view(request):
   # start_date = datetime.date(2000, 1, 1)
    #end_date = datetime.datetime.now()
   # posts=post.objects.filter(published_date__range=(start_date, end_date)) 
    posts= post.objects.filter(published_date__lte=datetime.datetime.now(),status=1)
    context={'posts':posts} 
    return render (request,'blog/blog-home.html',context)
      
              
def blog_single(request,pid):
    posts=get_object_or_404(post,pk=pid)
    if post:
        posts.counted_views = posts.counted_views + 1
        posts.save()
               
    context={'posts':posts}   
    return render (request,'blog/blog-single.html',context)

 
#def test (request,pid):
    #post=get_object_or_404(post,pk=pid)
    #context={'post':post}
    #return render (request,'test.html',context)
                    


