"""
views for newspaper application
"""
from django.shortcuts import render
from news.models import *


def index(request):
    """  Newspaper application index page view  """
    template_name = 'news/homepage.html'
    return render(request, template_name,
                  {'news_list': NewsBulletin.objects.all(), 'blog_list': Blog.objects.all(),
                   'article_list': Article.objects.all()}
                  )
