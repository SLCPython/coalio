#encoding: utf-8

from django.db import models

from coalio.models.mixins import TimestampMixin

class TaggedPost(TimestampMixin):
    ref_url = models.URLField(max_length=300)
    content = models.TextField(blank=True)

    tagged_by = models.ForeignKey('profiles.Coalio.User')

    def __unicode__(self):
        return "TaggedPost #%s from %s" % (self.id, self.ref_url)
