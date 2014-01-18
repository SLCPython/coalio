#encoding: utf-8

from django.shortcuts import render

from discussions.models import Discussion, Reply
from discussions.forms import ReplyForm

def view_discussion(request, id):
    template_name = 'discussions/discussion_view.html'
    ctx = {}
    discussion = Discussion.objects.get(id=id)
    ctx['discussion'] = Discussion.objects.get(id=id)

    reply_form = ReplyForm()
    ctx['reply_form'] = reply_form

    ctx['replies'] = Reply.objects.filter(discussion=discussion)

    if request.method == 'POST':
        reply_form = ReplyForm(request.POST)
        ctx['reply_form'] = reply_form
        if reply_form.is_valid:
            reply_form.author = request.user
            reply_form.discussion = discussion
            reply_form.save()

    return render(request, template_name, ctx)


def index(request):
    template_name = 'discussions/discussion_list.html'
    ctx = {}
    ctx['discussions'] = Discussion.objects.all()
    return render(request, template_name, ctx)
