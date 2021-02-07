from django.urls import path
from . import views

from rest_framework import routers
from .api import ProfileViewSet, PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('api/users', ProfileViewSet, 'profiles')
router.register('api/posts', PostViewSet, 'posts')
router.register('api/comments', CommentViewSet, 'comments')

urlpatterns = router.urls
