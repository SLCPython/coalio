#encoding: utf-8

from django.shortcuts import render
from pages.models import Page

def view_pages(request):
    template_name = "pages/list.html"
    ctx = {}
    ctx['pages'] = Page.objects.all()
    return render(request, template_name, ctx)

def view_page(request, slug):
    template_name = "pages/page.html"
    ctx = {}
    ctx['page'] = Page.objects.get(slug=slug)
    return render(request, template_name, ctx)