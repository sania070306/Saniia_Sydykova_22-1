# from django.http import HttpResponse
from django.shortcuts import render, redirect
from posts.models import Post, Comment, Hashtag
from posts.forms import PostCreateForm, CommentCreateForm
from users.utils import get_user_from_request
from django.views.generic import ListView, CreateView

# Create your views here.

PAGINATION_LIMIT = 4


class HashtagsView(ListView):
    model = Hashtag
    template_name = 'hashtags/hashtags.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'object_list': self.get_queryset(),
            'user': get_user_from_request(self.request)
        }


class PostsView(ListView):
    model = Post
    template_name = 'posts/posts.html'

    def get(self, request, *args, **kwargs):
        hashtag_id = self.request.GET.get('hashtag_id')
        search_text = self.request.GET.get('search')
        post = self.model.objects.filter(hashtag_id=hashtag_id) if hashtag_id else self.model.objects.all()
        page = int(request.GET.get('page', 1))

        if search_text:
            post = post.filter(title__icontains=search_text)

        max_page = round(post.__len__() / PAGINATION_LIMIT)

        post = post[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        context = {
            'hashtag_id': hashtag_id,
            'posts': post,
            'object_list': self.get_queryset(),
            'user': get_user_from_request(self.request),
            'current_page': page,
            'max_page': range(1, max_page + 1)
        }
        return render(request, self.template_name, context=context)



class PostDetailView(ListView, CreateView):
    model = Comment
    template_name = 'posts/detail.html'
    form_class = CommentCreateForm
    queryset = Comment.objects.filter()


    def get(self, request, *args, **kwargs):
        post = Post.objects.get(id=kwargs['id'])

        context = {
            'post': post,
            'comments': self.model.objects.filter(post=kwargs['id']),
            'form': self.form_class,
            'user': get_user_from_request(self.request)
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            self.model.objects.create(
                author_id=2,
                text=form.cleaned_data.get('text'),
                post_id=kwargs['id']
            )
            return redirect(f'/posts/{kwargs["id"]}/')
        else:
            return render(request, self.template_name, context=self.get_context_data(form=form))



class PostCreateView(ListView, CreateView):
    model = Post
    template_name = 'posts/create.html'
    form_class = PostCreateForm

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'form': kwargs['form'] if kwargs.get('form') else self.form_class,
            'user': get_user_from_request(self.request)
        }

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            self.model.objects.create(
                author_id=1,
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                date=form.cleaned_data.get('date'),
                hashtag_id=form.cleaned_data.get('hashtag')
            )
            return redirect('/posts')
        else:
            return render(request, self.template_name, context=self.get_context_data(form=form))
