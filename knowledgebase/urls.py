"""knowledgebase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/'
    	, include(admin.site.urls)),
    url(r'^$'
    	, views.home, name='home'),
    url(r'^search/$',
        views.search, name='search'),
# article urls
    url(r'^articles/$'
        , views.article_categories, name='article_categories'),
    url(r'^articles/(?P<slug>[\w-]+)/$'
        , views.article_category, name='article_category'),
    url(r'^articles/(?P<category_slug>[\w-]+)/(?P<pk>[0-9]+)/(?P<article_slug>[\w-]+)/$'
        , views.article, name='article'),
# video urls
    url(r'^videos/$'
        , views.video_categories, name='video_categories'),
     url(r'^videos/(?P<slug>[\w-]+)/$'
        , views.video_category, name='video_category'),  
    url(r'^videos/(?P<category_slug>[\w-]+)/(?P<pk>[0-9]+)/(?P<video_slug>[\w-]+)/$'
        , views.video, name='video'), 
# discussion urls
    url(r'^discussions/$'
        , views.discussion_categories, name='discussion_categories'),
    url(r'^discussions/intouch/$'
        , views.discussion_category, name='discussion_category'),
    url(r'^discussions/intouch/1/some-discussions/$'
        , views.discussion, name='discussion')
]
