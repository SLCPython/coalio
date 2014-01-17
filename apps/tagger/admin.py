#encoding: utf-8

from django.contrib import admin

from tagger.models import TaggedPost

class TaggedPostAdmin(admin.ModelAdmin):
	model = TaggedPost

admin.site.register(TaggedPost, TaggedPostAdmin)