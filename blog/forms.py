from django import forms
from blog.models import Comment
#from django.forms import ModelForm
from captcha.fields import CaptchaField

 
class CommentForm(forms.ModelForm):
    class Meta :
        
        
        model=Comment
        fields=['post','name','subject','message','email'] 