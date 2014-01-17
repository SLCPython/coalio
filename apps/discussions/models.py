#encoding: utf-8

from django.db import models

from coalio.models.mixins import TimestampMixin

class Discussion(TimestampMixin):
    tagged_post = models.ForeignKey('tagger.TaggedPost')

    def __unicode__(self):
        return "Discussion about %s" % (self.tagged_post)
