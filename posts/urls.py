from django.urls import path
from posts.views import (HashtagsView,
                         PostCreateView,
                         PostsView,
                         PostDetailView)


urlpatterns = [
    path('hasthags/', HashtagsView.as_view()),
    path('posts/', PostsView.as_view()),
    path('posts/<int:id>/', PostDetailView.as_view()),
    path('posts/create/', PostCreateView.as_view()),
]