from django.shortcuts import render

# Create your views here.

def views(request):

    return render(request, 'views.html', {})

def create(request):

    return render(request, 'create.html', {})


def edit(request):

    return render(request, 'edit.html', {})
