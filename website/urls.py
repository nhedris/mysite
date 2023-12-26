
from django.urls import path , include
from website.views import *
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap


app_name='website'

urlpatterns = [
   
    path('', index, name='index'),
    path('about', about ,name='about'),
    path('contact', contact , name='contact'),
    path('test', test_view , name='test'),
    path('newsletter', newsletter_view , name='newsletter'),
  



]