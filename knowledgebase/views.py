# -*- coding: utf-8 -*-
import operator
from functools import reduce

from django.db import models
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from knowledgebase.apps.articles.models import Article, Video

def home(request):
	recent_articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]
	article_count = Article.objects.all().count()
	article_category_count = Article.objects.distinct('category').count()
	recent_videos = Video.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]
	video_count = Video.objects.all().count()
	video_category_count = Video.objects.distinct('category').count()
	return render(request, 'knowledgebase/index.html'
		, {'article_count':article_count,'article_category_count':article_category_count
			, 'recent_articles':recent_articles, 'recent_videos':recent_videos
			, 'video_count':video_count, 'video_category_count':video_category_count})

def article(request, pk, article_slug, category_slug):
	article = get_object_or_404(Article, pk=pk)
	return render(request, 'knowledgebase/article.html'
		, {'article':article})

def article_categories(request):
	categories = Article.objects.filter(published_date__lte=timezone.now()).order_by().values('category__name','category__slug').annotate(count=models.Count('pk'))
	return render(request, 'knowledgebase/article_categories.html'
		, {'categories':categories})

def article_category(request,slug):
	articles = Article.objects.filter(published_date__lte=timezone.now(),category__slug=slug)
	return render(request, 'knowledgebase/article_category.html'
		, {'articles':articles})

def video(request, pk, video_slug, category_slug):
	video = get_object_or_404(Video, pk=pk)
	return render(request, 'knowledgebase/video.html'
		, {'video':video})

def video_categories(request):
	categories = Video.objects.filter(published_date__lte=timezone.now()).order_by().values('category__name','category__slug').annotate(count=models.Count('pk'))
	return render(request, 'knowledgebase/video_categories.html'
		, {'categories':categories})

def video_category(request, slug):
	videos = Video.objects.filter(published_date__lte=timezone.now(),category__slug=slug)
	return render(request, 'knowledgebase/video_category.html'
		, {'videos':videos})

def search(request):
	query = request.GET.get('q')
	if query:
		query_list = query.split()
		results = Article.objects.filter(reduce(lambda x,y: x | y, [Q(title__iregex="\y{0}\y".format(x))|Q(text__iregex="\y{0}\y".format(x)) for x in query_list]))
		results_count = results.count
	else:
		results = ""
		results_count = 0
	return render(request, 'knowledgebase/search_results.html'
		, {'results':results
		,'results_count':results_count
		,'query':query})
	pass;