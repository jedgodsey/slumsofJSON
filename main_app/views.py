from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Mc
from .fixtures.seed import all_mcs, all_posts, all_comments

def home(request):
    return render(request, 'home.html')

def mcs(request):
    print(request)
    return JsonResponse(all_users, safe=False)

def seed(request):
    for mc in all_mcs:
        add_mc(mc)
    for post in all_posts:
        add_post(post)
    for comment in all_comments:
        add_comment(comment)
    return HttpResponse('database seeded')

def add_mc(new_mc):
    mc_instance = Mc.objects.create(**new_mc)
    mc_instance.save()

def add_post(new_post):
    post_instance = Post.objects.create(**new_post)
    post_instance.save()

def add_comment(new_comment):
    comment_instance = Comment.objects.create(**new_comment)
    comment_instance.save()
