from django.shortcuts import render, redirect
from django.urls import reverse
from administrators.forms import BlogPostForm


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect(reverse('administrators:views'))
    form = BlogPostForm()
    category = dict(form.fields.get('category').choices) 
    for cat in category.values():
        print(cat)
    context = {
        "category": category
    }
    return render(request, 'clients/index.html', context)

def category(request, category):
    if request.user.is_authenticated:
        return redirect(reverse('administrators:views'))
    return render(request, 'clients/category.html', {})

def news(request):
    if request.user.is_authenticated:
        return redirect(reverse('administrators:views'))
    return render(request, 'clients/news.html', {})
