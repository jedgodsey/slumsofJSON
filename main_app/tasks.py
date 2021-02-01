def print_something():
    print('something')


def seed(request):
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
    new_post['profile'] = found_profile
    post_instance = Post.objects.create(**new_post)
    post_instance.save()

def add_comment(new_comment):
    found_profile = Profile.objects.get(id=new_comment['profile'])
    found_post = Post.objects.get(id=new_comment['post'])
    new_comment['profile'] = found_profile
    new_comment['post'] = found_post
    comment_instance = Comment.objects.create(**new_comment)
    comment_instance.save()

def reset(table):
    sequence_sql = connection.ops.sequence_reset_sql(no_style(), [table])
    with connection.cursor() as cursor:
        for sql in sequence_sql:
            cursor.execute(sql)
