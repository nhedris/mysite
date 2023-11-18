from django.shortcuts import render
from django.db import models
from blog import models
from blog.models import post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Crefrom django.http import HttpResponse,jsonResponse

def index (request): 
    posts= post.objects.filter(status=1)
    posts= Paginator(posts,3)
    try:
        page_number=request.GET.get('page') 
        posts= posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context={'posts':posts  }   
    return render (request,'website/index.html',context)

def about(request):
    return render (request,'website/about.html')

def contact(request):
    return render (request,'website/contact.html')