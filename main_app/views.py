from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Profile, Post, Comment
from .forms import ProfileForm, PostForm, CommentForm
from .fixtures.seed import all_profiles, all_posts, all_comments
import json
import time

from django.core.management.color import no_style
from django.db import connection

from django.core import serializers

def home(request):
    seed(request)
    return render(request, 'home.html')

def read(request):
    print('your request: ', request.__dict__)
    return HttpResponse('yes')

# def profiles(request):
#     response = json.dumps(list(Profile.objects.values()))
#     return HttpResponse(response, content_type='text/json')

# def new_profile(request):
#     add_profile(json.loads(request.body))
#     return HttpResponse(request.body, content_type='text/json')

# def show_profile(request, profile_id):
#     profile = Profile.objects.get(id=profile_id)
#     found_profile = {
#         'id': profile.id,
#         'name': profile.name,
#         'profile_name': profile.profile_name,
#         'email': profile.email
#     }
#     response = json.dumps(found_profile)
#     return HttpResponse(response, content_type='text/json')

# def edit_profile(request, profile_id):
#     found_profile = Profile.objects.get(id=profile_id)
#     # new_profile = ProfileForm(request.POST, request.FILES) #, instance=found_profile) # what are these parameters
#     new_profile = Profile(json.loads(request.body))
#     updated_profile = new_profile.save()

#     # if new_profile.is_valid():
#     #     updated_profile = new_profile.save()
#     #     # return HttpResponse(new_profile, content_type='text/json')
#     #     return HttpResponse('got here')
#     return HttpResponse(updated_profile, content_type='text/json')

#########################
# def edit_profile(request, profile_id):
#     # print(json.loads(request.body))
#     # print(request.body.decode('utf8'))
#     found_profile = Profile.objects.get(id=profile_id)
#     if request.method == 'POST':
#         profile_form = ProfileForm(request.POST, request.FILES, instance=found_profile)
#         print('profile_form.errors', profile_form.errors)
#         if  profile_form.is_valid():
#             updated_profile = profile_form.save()
#             return HttpResponse('step one')
#     form = ProfileForm(instance=found_profile)
#     return HttpResponse('step two')
#############################

def posts(request):
    return JsonResponse(all_posts, safe=False)

def comments(request):
    return JsonResponse(all_comments, safe=False)

def seed(request):
    print('seed request: ', request.__dict__)
    Profile.objects.all().delete()
    reset(Profile)
    for profile in all_profiles:
        add_profile(profile)
    Post.objects.all().delete()
    reset(Post)
    for post in all_posts:
        add_post(post)
    Comment.objects.all().delete()
    reset(Comment)
    for comment in all_comments:
        add_comment(comment)
    return HttpResponse('database cleared and seeded')

def add_profile(new_profile):
    profile_instance = Profile.objects.create(**new_profile)
    profile_instance.save()

def add_post(new_post):
    found_profile = Profile.objects.get(id=new_post['profile'])
    new_post = new_post.copy()
    new_post['profile'] = found_profile
    post_instance = Post.objects.create(**new_post)
    post_instance.save()

def add_comment(new_comment):
    found_profile = Profile.objects.get(id=new_comment['profile'])
    found_post = Post.objects.get(id=new_comment['post'])
    new_comment = new_comment.copy()
    new_comment['profile'] = found_profile
    new_comment['post'] = found_post
    comment_instance = Comment.objects.create(**new_comment)
    comment_instance.save()

def reset(table):
    sequence_sql = connection.ops.sequence_reset_sql(no_style(), [table])
    with connection.cursor() as cursor:
        for sql in sequence_sql:
            cursor.execute(sql)
