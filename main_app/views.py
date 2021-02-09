from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User, Post, Comment
from .forms import UserForm, PostForm, CommentForm
from .fixtures.seed import all_users, all_posts, all_comments
import json
import time

from django.core.management.color import no_style
from django.db import connection

from django.core import serializers

def home(request):
    seed(request)
    return render(request, 'home.html')
    
# def users(request):
#     response = json.dumps(list(User.objects.values()))
#     return HttpResponse(response, content_type='text/json')

# def new_user(request):
#     add_user(json.loads(request.body))
#     return HttpResponse(request.body, content_type='text/json')

# def show_user(request, user_id):
#     user = User.objects.get(id=user_id)
#     found_user = {
#         'id': user.id,
#         'name': user.name,
#         'user_name': user.user_name,
#         'email': user.email
#     }
#     response = json.dumps(found_user)
#     return HttpResponse(response, content_type='text/json')

# def edit_user(request, user_id):
#     found_user = User.objects.get(id=user_id)
#     # new_user = UserForm(request.POST, request.FILES) #, instance=found_user) # what are these parameters
#     new_user = User(json.loads(request.body))
#     updated_user = new_user.save()

#     # if new_user.is_valid():
#     #     updated_user = new_user.save()
#     #     # return HttpResponse(new_user, content_type='text/json')
#     #     return HttpResponse('got here')
#     return HttpResponse(updated_user, content_type='text/json')

#########################
# def edit_user(request, user_id):
#     # print(json.loads(request.body))
#     # print(request.body.decode('utf8'))
#     found_user = User.objects.get(id=user_id)
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, request.FILES, instance=found_user)
#         print('user_form.errors', user_form.errors)
#         if  user_form.is_valid():
#             updated_user = user_form.save()
#             return HttpResponse('step one')
#     form = UserForm(instance=found_user)
#     return HttpResponse('step two')
#############################

def posts(request):
    return JsonResponse(all_posts, safe=False)

def comments(request):
    return JsonResponse(all_comments, safe=False)

def seed(request):
    print('seed request: ', request.__dict__)
    User.objects.all().delete()
    reset(User)
    for user in all_users:
        add_user(user)
    Post.objects.all().delete()
    reset(Post)
    for post in all_posts:
        add_post(post)
    Comment.objects.all().delete()
    reset(Comment)
    for comment in all_comments:
        add_comment(comment)
    return HttpResponse('database cleared and seeded')

def add_user(new_user):
    user_instance = User.objects.create(**new_user)
    user_instance.save()

def add_post(new_post):
    found_user = User.objects.get(id=new_post['user'])
    new_post = new_post.copy()
    new_post['user'] = found_user
    post_instance = Post.objects.create(**new_post)
    post_instance.save()

def add_comment(new_comment):
    found_user = User.objects.get(id=new_comment['user'])
    found_post = Post.objects.get(id=new_comment['post'])
    new_comment = new_comment.copy()
    new_comment['user'] = found_user
    new_comment['post'] = found_post
    comment_instance = Comment.objects.create(**new_comment)
    comment_instance.save()

def reset(table):
    sequence_sql = connection.ops.sequence_reset_sql(no_style(), [table])
    with connection.cursor() as cursor:
        for sql in sequence_sql:
            cursor.execute(sql)
