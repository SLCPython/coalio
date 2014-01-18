#encoding: utf-8

from django.db import models

from discussions.utils import create_discussion
from tagger.models import TaggedPost

models.signals.post_save.connect(create_discussion, sender=TaggedPost)
