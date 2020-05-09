from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Post

def index(request):
    posts = Post.objects.all()
    print (posts.query)
    return render(request, 'index.html',  context={
        'posts': posts
    })

def about(request):
    return render(request, 'about.html',  context={})


def service(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')    
    return render(request, 'service.html',  context={})
