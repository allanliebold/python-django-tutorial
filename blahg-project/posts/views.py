# -*- coding: utf-8 -*-
"""Posts views."""


from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post


def home(request):
    """Home view."""
    posts = Post.objects.order_by('pub_date')
    return render(request, 'posts/home.html', {'posts': posts})
