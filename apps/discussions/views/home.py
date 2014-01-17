#encoding: utf-8

from django.shortcuts import render

def index(request):
    template_name = 'discussions/page.html'
    ctx = {}
    ctx['person'] = {
            'first_name': "Bob",
            'last_name': "Builder"
    }
    return render(request, template_name, ctx)
