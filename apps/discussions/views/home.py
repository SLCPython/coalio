#encoding: utf-8

from django.shortcuts import render
# from discussions.models import PageModel

def index(request):
    template_name = 'discussions/temp.html'
    ctx = {}
    ctx['person'] = {
            'first_name': "Bob",
            'last_name': "Builder"
    }
    return render(request, template_name, ctx)
