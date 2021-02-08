from django.urls import path
from . import views

from rest_framework import routers
from .api import ProfileViewSet, PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('users', ProfileViewSet, 'profiles')
router.register('posts', PostViewSet, 'posts')
router.register('comments', CommentViewSet, 'comments')

urlpatterns = router.urls
