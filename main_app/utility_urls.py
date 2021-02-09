from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # path('users/', views.users, name='users'),
    # path('users/new/', views.new_user, name='new_user'),
    # path('users/<int:user_id>/', views.show_user, name='show_user'),
    # path('users/<int:user_id>/edit/', views.edit_user, name='edit_user'),
    # path('users/<int:user_id>/delete/', views.delete_user, name='delete_user'),

    # path('posts/', views.posts, name='posts'),
    # path('posts/new/', views.new_post, name='new_post'),
    # path('posts/<int:post_id>/', views.show_post, name='show_post'),
    # path('posts/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    # path('posts/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    # path('posts/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),

    # path('comments/', views.comments, name='comments'),
    # path('comments/new/', views.new_comment, name='new_comment'),
    # path('comments/<int:comment_id>/', views.show_comment, name='show_comment'),
    # path('comments/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    # path('comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),

    path('seed/', views.seed)
]
