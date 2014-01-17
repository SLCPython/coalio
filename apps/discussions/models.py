#encoding: utf-8

from django.db import models
from django.core.urlresolvers import reverse

from coalio.models.mixins import TimestampMixin

class Discussion(TimestampMixin):
    tagged_post = models.ForeignKey('tagger.TaggedPost')

    def __unicode__(self):
        return "Discussion about %s" % (self.tagged_post)

    def get_absolute_url(self):
        return reverse('discussions:view', args=[self.id])
