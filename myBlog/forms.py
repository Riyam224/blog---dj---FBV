from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'add your message ',
        'row': 5,
        'column ': 120
    }))

    class Mata:
        model = Article
        fields = ['title', 'description']
