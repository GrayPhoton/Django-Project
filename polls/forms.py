from socket import fromshare
from django import forms

from .models import DeepThought

class deepThoughtForm(forms.ModelForm):
    class Meta:
        model=DeepThought
        fields=[
            'title',
            'thoughts',
        ]