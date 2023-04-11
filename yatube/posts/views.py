from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    """Главная страница."""
    posts = Post.objects.order_by('-pub_date')[:10]
    template = 'posts/index.html'
    context = {'posts': posts}
    return render(request, template, context)


def group_posts(request, slug):
    """Страницца группы."""
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:10]

    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
