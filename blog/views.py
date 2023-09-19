from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.http import Http404

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    total_num_blogs = blogs.count()
    return render(request, 'blog/index.html', {"title":"Tsune\'s Blog", "total_num_blogs": total_num_blogs, "blogs": blogs}) # return to html


def details(request, slug): # id -> slug # title -> id
    #blog = Blog.objects.filter(pk=id).first() 
    # try:
    #     blog = Blog.objects.get(pk=id)
    # except:
    #     raise Http404() # Http404 no argument
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, "blog/blog_detail.html", {"title":"Tsune\'s Blog", 
                                                     "blog_title": blog.title,
                                                     "blog_release": blog.release_date,
                                                     "blog_content": blog.content})
