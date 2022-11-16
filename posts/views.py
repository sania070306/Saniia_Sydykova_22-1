from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from posts.models import Post
# Create your views here.


def hashtags_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()

        data = {
            'posts': posts
        }
        return render(request, 'layouts/main.html', context=data)

def posts_view (request):
    if request.method == 'GET':
        posts = Post.objects.all()

        data = {
            'posts': posts
        }
        return render(request, 'posts/posts.html', context=data)


