from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Profile, Post, Comment
from .fixtures.seed import all_profiles, all_posts, all_comments

def home(request):
    return render(request, 'home.html')

def profiles(request):
    print(request)
    return JsonResponse(all_users, safe=False)

def seed(request):
    for profile in all_profiles:
        add_profile(profile)
    for post in all_posts:
        add_post(post)
    for comment in all_comments:
        add_comment(comment)
    return HttpResponse('database seeded')

def add_profile(new_profile):
    profile_instance = Profile.objects.create(**new_profile)
    profile_instance.save()

def add_post(new_post):
    post_instance = Post.objects.create(**new_post)
    post_instance.save()

def add_comment(new_comment):
    comment_instance = Comment.objects.create(**new_comment)
    comment_instance.save()
