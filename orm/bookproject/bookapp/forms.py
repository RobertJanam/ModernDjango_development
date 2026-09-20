from django import forms

class BookForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    author = forms.CharField(label='Author', max_length=100)
    price = forms.IntegerField(label='Price')
    publisher = forms.CharField(label='Publisher', max_length=100)
    ebook = forms.BooleanField(initial=True)