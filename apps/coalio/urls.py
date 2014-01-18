#encoding: utf-8
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from tagger.views.api import TaggedPostResource

admin.autodiscover()

tagged_post = TaggedPostResource()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'profiles.views.home.login_view', name='home'),
    url(r'^profiles/', include('profiles.urls', namespace='profiles')),
    url(r'^accounts/login/$', 'profiles.views.home.login_view', name='login'),
    url(r'^taggedposts/', include('tagger.urls', namespace='tagger')),
    url(r'^discussion/', include('discussions.urls', namespace='discussions')),
    url(r'^pages/', include('pages.urls', namespace='pages')),

    # API urls
    url(r'^api/', include(tagged_post.urls)),

    # 3rd party urls
    url(r'^search/', include('haystack.urls', namespace='search')),

    # admin urls
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
