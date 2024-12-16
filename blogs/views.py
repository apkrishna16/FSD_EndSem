from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog(request): 
    blogs = Blog.objects.all().order_by('-created_at')   
    return render(request, 'blogs.html', {'blogs': blogs})

def blog_content(request, blog_id): 
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog_content.html', {'blog': blog})
