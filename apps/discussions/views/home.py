#encoding: utf-8

from django.shortcuts import render

def index(request):
    ctx = {}
    ctx['person'] = {
            'first_name': "Bob",
            'last_name': "Builder"
    }
    return render(request, 'discussions/temp.html', ctx)
