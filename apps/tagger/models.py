#encoding: utf-8

from django.db import models

from coalio.models.mixins import TimestampMixin

from taggit.managers import TaggableManager


class TaggedPost(TimestampMixin):
    ref_url = models.URLField(max_length=300)
    content = models.TextField(blank=True)
    bully_social_id = models.CharField(max_length=200, blank=True, default='')

    tagged_by = models.ForeignKey('profiles.CoalioUser')
    tags = TaggableManager()

    def __unicode__(self):
        return "TaggedPost #%s from %s" % (self.id, self.ref_url)
