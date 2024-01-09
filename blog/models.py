from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class category(models.Model):
    name=models.CharField(max_length=255)
        
    def __str__(self):
          return self.name
      
class post (models.Model):
    title= models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    content= models.TextField()
    tags = TaggableManager()
    image=models.ImageField(upload_to='blog/')
    category=models.ManyToManyField(category)
    counted_views = models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    login_require=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    published_date=models.DateTimeField( null=True)
    
     
    class Meta:
        ordering=['created_date']
     
    def __str__(self):
        return self.title
    def get_abdolute_url(self):
        return reverse ('blog:single',kwargs={'pid':self.id})
      

class Comment (models.Model):
    post=models.ForeignKey(post,on_delete=models.CASCADE)
    name= models.CharField(max_length=255)
    email=models.EmailField()
    subject= models.CharField(max_length=255)
    message= models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    approved=models.BooleanField(default=False)
    
    class Meta:
        ordering=['created_date']
        
    def __str__(self):
        return self.name