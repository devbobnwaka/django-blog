from django.db import models
from django.db.models.signals import pre_save, post_save
from django.conf import settings

from .utils import slugify_instance_title
User = settings.AUTH_USER_MODEL

# Create your models here.
class BlogPost(models.Model):
    NEWS = 'NE'
    SPORTS = 'SP'
    POLITICS = 'PO'
    BUSINESS = 'BU'
    CATEGORY_CHOICES = [
        (NEWS,"News"),
        (SPORTS,"Sports"),
        (POLITICS,"Politics"),
        (BUSINESS,"Business"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True, unique=True)
    reporter_name = models.CharField(max_length=100)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=NEWS,)
    blog_content = models.TextField()
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     if self.slug:
    #         self.slug = slugify(self.title)
    #if I am to use the slugify_instance_title function here
        # if self.slug is None:
        #     slugify_instance_title(instance)
    #     super().save(*args, **kwargs)

def blog_post_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance)

pre_save.connect(blog_post_pre_save, sender=BlogPost) 

def blog_post_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)

post_save.connect(blog_post_post_save, sender=BlogPost) 

