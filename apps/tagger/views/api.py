#encoding: utf-8

from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization

from tagger.models import TaggedPost

class TaggedPostResource(ModelResource):
    class Meta:
        queryset = TaggedPost.objects.all()
        resource_name = 'tagged_post'
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
