from django.urls import path
from . import views

from rest_framework import routers
from .api import UserViewSet, PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet, 'users')
router.register('posts', PostViewSet, 'posts')
router.register('comments', CommentViewSet, 'comments')

urlpatterns = router.urls
