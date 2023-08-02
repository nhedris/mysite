from django.shortcuts import render

# Crefrom django.http import HttpResponse,jsonResponse

def home(request):
   return render (request,'website/index.html')

def about(request):
    return render (request,'website/about.html')

def contact(request):
    return render (request,'website/contact.html')