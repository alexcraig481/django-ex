from django import forms
from .models import Log


class EntryForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
