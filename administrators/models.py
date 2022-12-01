from django.db import models

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
    title = models.CharField(max_length=100)
    reporter_name = models.CharField(max_length=100)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=NEWS,)
    blog_content = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
