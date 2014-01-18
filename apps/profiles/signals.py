#encoding: utf-8
from django.db import models

from profiles.models import CoalioUser
from tastypie.models import create_api_key

models.signals.post_save.connect(create_api_key, sender=CoalioUser)
