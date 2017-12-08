# -*- coding: utf-8 -*-
"""Posts views."""


from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):
    """Home view."""
    posts = Post.objects.order_by('pub_date')
    return render(request, 'posts/home.html', {'posts': posts})


def post_detail(request, post_id):
    """View for specific post."""
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})
