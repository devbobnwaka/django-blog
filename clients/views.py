from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from administrators.forms import BlogPostForm
from administrators.models import BlogPost

def context_category():
    form = BlogPostForm()
    return dict(form.fields.get('category').choices) 

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect(reverse('administrators:views'))
    blogs = BlogPost.objects.all().order_by('-id')
    paginator = Paginator(blogs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.GET.get('slug'):
        blog = BlogPost.objects.get(slug=request.GET.get('slug'))
    else:
        blog = blogs.first()

    context = {
        "category": context_category(),
        "blogs": page_obj,
        "blog": blog,
        "blogs": page_obj
    }
    return render(request, 'clients/index.html', context)

def category(request, category, key):
    if request.user.is_authenticated:
        return redirect(reverse('administrators:views'))
    blogs = BlogPost.objects.filter(category=key).order_by('-id')
    paginator = Paginator(blogs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.GET.get('slug'):
        blog = BlogPost.objects.get(slug=request.GET.get('slug'))
    else:
        blog = blogs.first()

    context = {
        "category": context_category(),
        "topic": category,
        "blog": blog,
        "blogs": page_obj
    }
    return render(request, 'clients/category.html', context)

def news(request):
    if request.user.is_authenticated:
        return redirect(reverse('administrators:views'))

    context = {
        "category": context_category()
    }
    return render(request, 'clients/news.html', context)
