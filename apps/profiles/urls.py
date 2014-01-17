# encoding: utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns('profiles.views.home',
    url(r'^$', 'index', name='home'),
    url(r'^change_password/$', 'change_password', name='change_password'),
    url(r'^logout/$', 'logout_view', name='logout')
)
