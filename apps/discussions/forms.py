#encoding=utf-8

from django import forms

from models import Reply

class ReplyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReplyForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['class'] = 'form-control'
    class Meta:
        model = Reply
        exclude = ('author', 'discussion')

