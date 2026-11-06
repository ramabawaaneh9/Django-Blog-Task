
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    UserViewSet,
    CategoryViewSet,
    PostViewSet,
    CommentViewSet,
)

from .views.generate import generate_post
from .views.summarize import summarize_post_view


router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register('categories', CategoryViewSet, basename='categories')
router.register('posts', PostViewSet, basename='posts')
router.register('comments', CommentViewSet, basename='comments')


urlpatterns = [
    path(
        'posts/<int:post_id>/summarize/',
        summarize_post_view,
        name='summarize-post'
    ),

    path(
        'posts/generate/',
        generate_post,
        name='generate-post'
    ),

    path('', include(router.urls)),
]
