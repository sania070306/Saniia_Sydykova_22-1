from django.urls import path
from posts.views import hashtags_view, posts_view


urlpatterns = [
    path('hasthags/', hashtags_view),
    path('posts/', posts_view)
]