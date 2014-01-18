# encoding: utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns('tagger.views.director',
    url(r'^(?P<id>\d+)$', 'direct_to_discussion', name='director'),
)
