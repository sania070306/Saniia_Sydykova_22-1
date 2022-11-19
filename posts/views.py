from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from posts.models import Post, Comment
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


def post_detail_view(request, **kwargs):
    if request.method == 'GET':
        post = Post.objects.get(id=kwargs['id'])
        comments = Comment.objects.filter(post=kwargs['id'])

        data = {
            'post': post,
            'comments': comments
        }

        return render(request, 'posts/detail.html', context=data)
