#encoding: utf-8

from django.shortcuts import render

from discussions.models import Discussion

def view_discussion(request, id):
    template_name = 'discussions/discussion_view.html'
    ctx = {}
    ctx['discussion'] = Discussion.objects.get(id=id)
    return render(request, template_name, ctx)


def index(request):
    template_name = 'discussions/discussion_list.html'
    ctx = {}
    ctx['discussions'] = Discussion.objects.all()
    return render(request, template_name, ctx)
