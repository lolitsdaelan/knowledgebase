# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from knowledgebase.apps.articles.models import Article

def home(request):
	articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	categories = Article.objects.filter(published_date__lte=timezone.now()).distinct('category')
	return render(request, 'knowledgebase/index.html'
		, {'articles':articles,'categories':categories})

def article(request, pk, slug):
	article = get_object_or_404(Article, pk=pk)
	return render(request, 'knowledgebase/article.html'
		, {'article':article})

def articles(request):
	categories = Article.objects.filter(published_date__lte=timezone.now()).distinct('category')
	return render(request, 'knowledgebase/articles.html'
		, {'categories':categories})