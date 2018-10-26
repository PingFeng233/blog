import math
import markdown
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category, Labels
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from blog.settings import PER_NUM, MAX_PAGE
from utils import custom_paginator
from userview.utils import change_info


# Create your views here.

def aside_data():
    posts = Post.objects.filter(active=True).order_by('-id')
    categories = Category.objects.all()
    last_posts = posts.order_by('-created_time')[:5]
    rank_posts = posts.order_by('-view_nums')[:5]
    return posts, categories, last_posts, rank_posts


# 分页
def pagination(request, post_list):
    cur_page = int(request.GET.get('page', 1))
    total_page = math.ceil(len(post_list) / PER_NUM)
    start, end = custom_paginator(cur_page, total_page, MAX_PAGE)
    page_range = range(start, end + 1)
    posts = post_list[(cur_page - 1) * PER_NUM: cur_page * PER_NUM]
    prev = cur_page - 1 if cur_page - 1 >= 1 else 1
    next = cur_page + 1 if cur_page + 1 <= total_page else total_page
    return start, end, page_range, posts, prev, next, cur_page


# 渲染markdown
def render_markdown(content):
    content = markdown.markdown(content, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'])
    return content


def index(request, **kwargs):
    change_info(request)
    post_list, categories, last_posts, rank_posts = aside_data()
    start, end, page_range, posts, prev, next, cur_page = pagination(request, post_list)
    for post in posts:
        post.content = render_markdown(post.content)
    return render(request, 'posts/index.html', locals())


def detail(request, id):
    post = get_object_or_404(Post, id=id)
    post.increase_view()
    post.content = render_markdown(post.content)
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
    posts_aside, categories, last_posts, rank_posts = aside_data()
    post_list = category.post_set.all()
    start, end, page_range, posts, prev, next, cur_page = pagination(request, post_list)
    for post in posts:
        post.content = render_markdown(post.content)
    return render(request, 'posts/categories.html', locals())


def search(request):
    kw = request.GET.get('kw', None)
    post_all, categories, last_posts, rank_posts = aside_data()
    if kw:
        post_list = Post.objects.filter(Q(title__contains=kw) | Q(content__contains=kw))
    else:
        post_list = []
    start, end, page_range, posts, prev, next, cur_page = pagination(request, post_list)
    for post in posts:
        post.content = render_markdown(post.content)
    return render(request, 'posts/search.html', locals())


def about(request):
    post_all, categories, last_posts, rank_posts = aside_data()
    return render(request, 'posts/about.html', locals())
