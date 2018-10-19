from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category, Labels
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q


# Create your views here.

def aside_data():
    posts = Post.objects.filter(active=True)
    categories = Category.objects.all()
    last_posts = posts.order_by('-created_time')[:5]
    rank_posts = posts.order_by('-view_nums')[:5]
    return posts, categories, last_posts, rank_posts


def index(request):
    posts, categories, last_posts, rank_posts = aside_data()
    return render(request, 'posts/index.html', locals())


def detail(request, id):
    post = Post.objects.get(id=id)
    posts, categories, last_posts, rank_posts = aside_data()
    try:
        prev = Post.objects.get(id=int(id) - 1)
    except ObjectDoesNotExist:
        prev = None
    try:
        next = Post.objects.get(id=int(id) + 1)
    except ObjectDoesNotExist:
        next = None
    return render(request, 'posts/detail.html', locals())


def categories(request, pk):
    category = Category.objects.get(pk=pk)
    posts, categories, last_posts, rank_posts = aside_data()
    posts = category.post_set.all()
    return render(request, 'posts/categories.html', locals())


def search(request):
    kw = request.GET.get('kw', None)
    post_all, categories, last_posts, rank_posts = aside_data()
    if kw:
        posts = Post.objects.filter(Q(title__contains=kw) | Q(content__contains=kw))
    return render(request, 'posts/search.html', locals())
