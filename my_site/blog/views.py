from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html', {"title":"Tsune\'s Blog"}) # return to html