from django.shortcuts import render, redirect
from django.urls import reverse
from administrators.forms import BlogPostForm

def context_category():
    form = BlogPostForm()
    return dict(form.fields.get('category').choices) 

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect(reverse('administrators:views'))
    
    context = {
        "category": context_category()
    }
    return render(request, 'clients/index.html', context)

def category(request, category):
    if request.user.is_authenticated:
        return redirect(reverse('administrators:views'))

    context = {
        "category": context_category()
    }
    return render(request, 'clients/category.html', context)

def news(request):
    if request.user.is_authenticated:
        return redirect(reverse('administrators:views'))

    context = {
        "category": context_category()
    }
    return render(request, 'clients/news.html', context)
