from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Profile, Post, Comment
from .forms import ProfileForm, PostForm, CommentForm
from .fixtures.seed import all_profiles, all_posts, all_comments
import json

def home(request):
    return render(request, 'home.html')

def profiles(request):
    profiles = Profile.objects.all()
    form = ProfileForm()
    context = {
        'form': form,
        'profiles': profiles
    }
    print(context)
    # return JsonResponse(context, safe=False)
    return HttpResponse(context)

def city_index(request):
    all_cities = City.objects.all()
    form = CityForm()
    context = {
        'form' : form,
        'cities': all_cities
    }
    return render(request,'cities/index.html',context)

def new_profile(request):
    print('in new_profile')
    add_profile(json.loads(request.body))
    return HttpResponse('safe at last')

def show_profile(request):
    return JsonResponse(all_profiles, safe=False)

def edit_profile(request):
    return JsonResponse(all_profiles, safe=False)

def delete_profile(request):
    return JsonResponse(all_profiles, safe=False)



def posts(request):
    return JsonResponse(all_posts, safe=False)

def comments(request):
    return JsonResponse(all_comments, safe=False)

def seed(request):
    for profile in all_profiles:
        add_profile(profile)
    for post in all_posts:
        add_post(post)
    for comment in all_comments:
        add_comment(comment)
    return HttpResponse('database seeded')

def add_profile(new_profile):
    print('in add_profile')
    profile_instance = Profile.objects.create(**new_profile)
    profile_instance.save()

def add_post(new_post):
    post_instance = Post.objects.create(**new_post)
    post_instance.save()

def add_comment(new_comment):
    comment_instance = Comment.objects.create(**new_comment)
    comment_instance.save()
