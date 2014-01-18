#encoding: utf-8

# Redirects to the discussion
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from discussions.models import Discussion

def direct_to_discussion(request, id):
    discussion = Discussion.objects.get(tagged_post__id=id)
    disc_id = discussion.id
    return redirect(reverse('discussions:view', kwargs={'id': disc_id}))
