from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .utils import form_fields, form_select_fields
from .forms import BlogPostForm

# Create your views here.
@login_required
def views(request):
    
    return render(request, 'views.html', {})

def create(request):
    form = BlogPostForm(request.POST or None)
    category = dict(form.fields.get('category').choices) 
    context = {
        "form": form,
        "cats": category,
    }
    
    form_fields('title', form, 'Title')
    form_fields('reporter_name', form, 'Reporter name')
    form_fields('blog_content', form, 'Blog content here...')
    form_fields('image', form, 'image')
    form_select_fields('category', form, 'Category')

    return render(request, 'create.html', context)


def edit(request):

    return render(request, 'edit.html', {})
