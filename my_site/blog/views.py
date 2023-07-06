from django.shortcuts import render
from .models import Blog

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/index.html', {"title":"Tsune\'s Blog", "blogs": blogs}) # return to html


def details(request, title):
    blog = Blog.objects.filter(title=title).first()
    return render(request, "blog/blog_detail.html", {"title":"Tsune\'s Blog", "blog": blog})