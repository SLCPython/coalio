# encoding: utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns('discussions.views.home',
    url(r'^(?P<id>\d+)$', 'view_discussion', name='view'),
    url(r'^$', 'index', name='home'),
)
