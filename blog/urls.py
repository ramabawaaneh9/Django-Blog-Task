from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    UserViewSet,
    CategoryViewSet,
    PostViewSet,
    CommentViewSet,
)


router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register('categories', CategoryViewSet, basename='categories')
router.register('posts', PostViewSet, basename='posts')
router.register('comments', CommentViewSet, basename='comments')


urlpatterns = [
    path('', include(router.urls)),
]