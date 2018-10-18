from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category,Labels


# Create your views here.

def index(request):
    posts = Post.objects.filter(active=True)
    categories = Category.objects.all()
    last_posts = posts.order_by('-created_time')[:5]
    return render(request, 'posts/index.html', locals())


def detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'posts/detail.html', locals())
