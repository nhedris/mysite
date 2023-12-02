from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.db import models
from blog import models
from blog.models import post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from website.models import Contact
from website.forms import ContactForm, NewsletterForm
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser


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
     if request.method=="POST" :
          form= ContactForm(request.POST, request.FILES)
          if form.is_valid():
              form.instance.name='unknown'
              form.save()
              messages.add_message(request,messages.SUCCESS,'your ticked submited successfully')   
          else:
               messages.add_message(request,messages.ERROR,'your ticked did not submited')
     form= ContactForm( )
     
     
     return render (request,'website/contact.html')

def test_view(request):
    if request.method=="POST" :
      form= ContactForm(request.POST)
      if form.is_valid():
          form.save()
          return HttpResponse('done')
      else: 
          return HttpResponse('not valid')
    form= ContactForm()
    return render (request,'test.html',{'form':form})   

def newsletter_view(request):
     if request.method=="POST" :
          form= NewsletterForm(request.POST)
     if form.is_valid():
          form.save()
          return HttpResponseRedirect('/')
     else: 
          return HttpResponseRedirect('/')
   
    