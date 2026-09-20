from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    title = forms.CharField(label='Title', max_length=100)
    author = forms.CharField(label='Author', max_length=100)
    price = forms.IntegerField(label='Price')
    publisher = forms.CharField(label='Publisher', max_length=100)
    ebook = forms.BooleanField(initial=True)
    
    class Meta:
        model = Book
        # fields = "__all__" # when you want to include all fields
        # fields = ["author", "title"] # when you want to include some
        exclude = ["id"] # when you want to exclude a field