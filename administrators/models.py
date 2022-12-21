from django.db import models
from django.utils import timezone
import math
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from django.conf import settings

from .utils import slugify_instance_title, unique_filename
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
    image = models.ImageField(upload_to=unique_filename("images"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("administrators:edit", kwargs={"slug": self.slug})
    

    def __str__(self):
        return self.title

    def whenPublished(self):
        now = timezone.now()
        
        diff= now - self.updated_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            if seconds == 1:
                return str(seconds) +  "second ago"
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)
            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)
            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
            if days == 1:
                return str(days) + " day ago"
            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years= math.floor(diff.days/365)
            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"

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

