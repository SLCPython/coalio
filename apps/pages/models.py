#encoding: utf-8

from django.db import models
from django.core.urlresolvers import reverse

from coalio.models.mixins import TimestampMixin

class Page(TimestampMixin):
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	content = models.TextField(blank=True)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('pages:view', args=[self.slug])