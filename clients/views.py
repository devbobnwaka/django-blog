from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect(reverse('administrators:views'))
    return render(request, 'clients/index.html', {})

def category(request):
    if request.user.is_authenticated:
        return redirect(reverse('administrators:views'))
    return render(request, 'clients/category.html', {})

def news(request):
    if request.user.is_authenticated:
        return redirect(reverse('administrators:views'))
    return render(request, 'clients/news.html', {})
