# -*- coding: utf-8 -*-
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from knowledgebase.apps.articles.models import Article

def home(request):
	recent_articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]
	article_count = Article.objects.all().count()
	category_count = Article.objects.distinct('category').count()
	return render(request, 'knowledgebase/index.html'
		, {'article_count':article_count,'category_count':category_count
			, 'recent_articles':recent_articles})

def article(request, pk, slug):
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