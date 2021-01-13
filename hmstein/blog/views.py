from django.shortcuts import render

from .models import Post

def index(request):
    latest_blog_posts = Post.objects.all().order_by('-pub_date')[:5]
    context = {'latest_blog_posts':latest_blog_posts }
    return render(request, 'blog/index.html', context)