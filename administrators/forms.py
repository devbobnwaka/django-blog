from django import forms
from .models import BlogPost
from django.forms import ImageField, FileInput

class BlogPostForm(forms.ModelForm):
    image =  ImageField(widget=FileInput) #ADDED TO REMOVE THE CURRENT IMAGE LABEL IN EDIT
    class Meta:
        model = BlogPost
        fields = ('title', 'reporter_name', 'category', 'blog_content', 'image')