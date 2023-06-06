from django import forms
from django.conf import settings

from .models import Topic, Entry, MyModel

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

class MyForm(forms.Form):
    class Meta:
        model = MyModel
        fields = ['file']