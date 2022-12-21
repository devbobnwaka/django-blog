from django.contrib import admin
from .models import BlogPost

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'reporter_name', 'category', 'blog_content', 'slug', 'updated_at' ]
    search_fields = ['title', 'blog_content']
     
admin.site.register(BlogPost, BlogPostAdmin)