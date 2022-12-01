from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'clients/index.html', {})

def category(request):

    return render(request, 'clients/category.html', {})

def news(request):

    return render(request, 'clients/news.html', {})
