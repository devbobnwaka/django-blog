from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .utils import form_fields, form_select_fields
from django.core.paginator import Paginator
from .forms import BlogPostForm
from .models import BlogPost

# Create your views here.
@login_required
def views(request):
    blogs = BlogPost.objects.all()
    paginator = Paginator(blogs, 10)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "blogs": page_obj,
    }
    return render(request, 'views.html', context)

@login_required
def create(request):
    form = BlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        blog = form.save(commit=False)
        blog.user = request.user
        blog.save()
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

@login_required
def edit(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostForm(request.POST or None, request.FILES or None, instance=blog)
    if form.is_valid():
        blog = form.save(commit=False)
        blog.user = request.user
        blog.save()
    context = {
        'blog':blog,
        'form':form
    }
    form_fields('title', form, 'Title')
    form_fields('reporter_name', form, 'Reporter name')
    form_fields('blog_content', form, 'Blog content here...')
    form_fields('image', form, 'image')
    form_select_fields('category', form, 'Category')

    return render(request, 'edit.html', context)

@login_required
def delete(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        # delete the blog from the database
        blog.delete()
        # redirect to the blog list
        return redirect(reverse('administrators:views'))
    return render(request, 'delete.html', {})
