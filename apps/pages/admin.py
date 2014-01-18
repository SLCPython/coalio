#encoding: utf-8

from django.contrib import admin

from pages.models import Page 

class PageAdmin(admin.ModelAdmin):
	model = Page 

admin.site.register(Page, PageAdmin)
