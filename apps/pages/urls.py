# endoding: utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns('pages.views.pages_view',
	url(r'^(?P<slug>[\w-]+)$', 'view_page', name='view'),
	url(r'^$', 'view_pages', name='home'),
)