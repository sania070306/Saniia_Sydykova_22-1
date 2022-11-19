from django.urls import path
from posts.views import hashtags_view, posts_view, post_detail_view


urlpatterns = [
    path('hasthags/', hashtags_view),
    path('posts/', posts_view),
    path('posts/<int:id>/', post_detail_view)
]