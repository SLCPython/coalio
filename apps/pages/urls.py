# endoding: utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns('pages.views.pages',
	url(r'^(?P<slug>[\w-]+)$', 'page', name='view'),
	url(r'^$', 'pages', name='home'),
)