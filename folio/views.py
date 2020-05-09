from django.shortcuts import render
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
    return render(request, 'service.html',  context={})
