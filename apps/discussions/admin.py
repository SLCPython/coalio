#encoding: utf-8

from django.contrib import admin

from discussions.models import Discussion

class DiscussionAdmin(admin.ModelAdmin):
	model = Discussion

admin.site.register(Discussion, DiscussionAdmin)