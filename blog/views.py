from django.shortcuts import render, get_object_or_404
import blog

from blog.models import Blog
from django import urls

def all_blogs(request):
    #posts = Blog.objects.order_by("-title")[:3] show the first 3 posts ordered by title reverse
    posts = Blog.objects.all()
    context = {'blogs': posts}
    return render(request, 'blog/all_blogs.html', context)

def detail(request, blog_id):
    # note that the parameter cited in the urls (blog_id)
    # MUST be contained in the function definition!
    blog = get_object_or_404(Blog, pk=blog_id)
    #get_object_or_404 return the object or a 404 error if it does not exist
    # we pass to this method the type of objects and its primary key pk
    context = {'blog': blog}
    
    return render(request, 'blog/detail.html', context)
