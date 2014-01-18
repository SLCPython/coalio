#encoding: utf-8

from django.contrib import admin

from discussions.models import Discussion, Reply

class DiscussionAdmin(admin.ModelAdmin):
	model = Discussion

class ReplyAdmin(admin.ModelAdmin):
    model = Reply

admin.site.register(Reply, ReplyAdmin)
admin.site.register(Discussion, DiscussionAdmin)