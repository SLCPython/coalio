#encoding:utf-8

from discussions.models import Discussion

def create_discussion(sender, instance, created, raw, using, **kwargs):
    """
    creates a discussion based on a tagged_post object
    """
    discussion = Discussion()
    discussion.tagged_post = instance
    discussion.save()
    return