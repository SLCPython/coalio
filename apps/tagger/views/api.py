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

    def obj_create(self, bundle, **kwargs):
        return super(TaggedPostResource, self).obj_create(bundle, tagged_by=bundle.request.user)
