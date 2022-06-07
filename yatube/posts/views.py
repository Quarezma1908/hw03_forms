from tokenize import group
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Group, Post


# Главная страница
def index(request):    
    posts = Post.objects.order_by('-pub_date')[:10]
    template = 'posts/index.html'
    text = f'Главная страница'
    context = {
        'text': text,
        'posts': posts,
    }
    return render(request, template, context) 

#def group_posts(request, **kwargs): kwargs['slug_name']
def group_posts(request, slug):
    template = 'posts/group_list.html'
    text = f'Вложенная страница'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'text': text,
        'group': group,
        'posts': posts,
        'slug_name': slug,
    }
    return render(request, template, context)