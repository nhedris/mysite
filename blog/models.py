from django.db import models
from django.contrib.auth.models import User

class category(models.Model):
    name=models.CharField(max_length=255)
        
    def __str__(self):
          return self.name
      

class post (models.Model):
    title= models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    content= models.TextField()
    image=models.ImageField(upload_to='blog/')
    category=models.ManyToManyField(category)
    counted_views = models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    published_date=models.DateTimeField( null=True)
    
     
class Meta:
         ordering=['created_date']
     
def __str__(self):
          return self.title
      
