from django.shortcuts import render,get_object_or_404,redirect
from blog.models import post,Comment
from django.utils import timezone
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from blog.forms import CommentForm
from django.contrib import messages


 

def blog_view(request,**kwargs):
    posts= post.objects.filter(published_date__lte=timezone.now(),status=1)
    if kwargs.get('cat_name')!= None :    
        posts= posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get ('author_username')!= None :  
        posts= posts.filter(author__username=kwargs['author_username']) 
    if  kwargs.get ('tag_name')!= None : 
        posts= posts.filter(tags__name__in=[kwargs['tag_name']])     
         
    posts= Paginator(posts,3)
    try:
       page_number=request.GET.get('page') 
       posts= posts.get_page(page_number)
    except PageNotAnInteger:
       posts = posts.get_page(1)
    except EmptyPage:
       posts = posts.get_page(1)
    
    context={'posts':posts , 'page_number':page_number }   
    return render (request,'blog/blog-home.html',context)
      
              
def blog_single(request,pid):
     if request.method == 'POST':
         form=CommentForm(request.POST)
         if form.is_valid():
             form.save()
             messages.add_message(request,messages.SUCCESS,'your comment submited successfully')   
         else:
             messages.add_message(request,messages.ERROR,'your comment did not submited')  
              
     posts=get_object_or_404(post,pk=pid,status=1,published_date__lte=timezone.now())
     if not post.login_require:
       comments= Comment.objects.filter(post=posts.id,approved=True)
       if post:
         posts.counted_views = posts.counted_views + 1
         posts.save()
       related_posts= post.objects.filter(published_date__lte=timezone.now(),status=1)
       nextp= related_posts.filter(id__gt=posts.id).order_by('id').first()
       previous=related_posts.filter(id__lt=posts.id).order_by('id').last()  
       form=CommentForm()         
       context={'posts':posts ,'nextp': nextp ,'previous': previous , 'comments' : comments ,'form':form}   
       return render (request,'blog/blog-single.html',context)
     else:
         return redirect('accounts/login')

def blog_category(request,cat_name):
       
    posts= post.objects.filter(status=1)
    posts= posts.filter(category__name=cat_name)
    context={'posts':posts} 
    return render (request,'blog/blog-home.html',context)
       

def blog_search(request):
    posts= post.objects.filter(status=1)
    if request.method== 'GET':
       if request.GET.get('s'): 
         posts=posts.filter(content__contains=request.GET.get('s'))
     
    context={'posts':posts} 
    return render (request,'blog/blog-home.html',context) 
              
 
       
  
def test (request):
    return render (request,'test.html')


                    


