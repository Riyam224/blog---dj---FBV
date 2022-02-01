from django import forms

from .models import Product


class ProductForm(forms.ModelForm):

    title = forms.CharField(label='', widget=forms.TextInput(attrs={
        "placeholder": "your title"
    }))
    email = forms.EmailField()
    desc = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "class": "new-class-name two",
        "id": "my-id-for-textarea",
        "rows": 20,
        "column": 120,
        "placeholder": "your textarea"
    }))
    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = ['title', 'desc', 'price']

    # TODO  to get title with CFE the first letter

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not "CFE" in title:
            raise forms.ValidationError('this is not valid title  ')
        if not "news" in title:
            raise forms.ValidationError('this is not valid title  ')
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith("edu"):
            raise forms.ValidationError('this is not valid email')
        return email


class RawForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={
        "placeholder": "your title"
    }))
    email = forms.EmailField()
    desc = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "class": "new-class-name two",
        "id": "my-id-for-textarea",
        "rows": 20,
        "column": 120,
        "placeholder": "your textarea"
    }))
    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = ['title', 'desc', 'price']
