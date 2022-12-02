from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def views(request):

    return render(request, 'views.html', {})

def create(request):

    return render(request, 'create.html', {})


def edit(request):

    return render(request, 'edit.html', {})
