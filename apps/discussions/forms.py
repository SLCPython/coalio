#encoding=utf-8

from django import forms

from models import Reply

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        exclude = ('author', 'discussion')

