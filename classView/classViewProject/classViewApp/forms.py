from django import forms
from .models import Book

# removed the field attributes and replaced them with the class meta fields and labels
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'publisher', 'coverimg', 'ebook'] # excludes 'id'
        
        labels = {
            'title': 'Title',
            'author': 'Author',
            'price': 'Price',
            'publisher': 'Publisher',
            'coverimg': 'Cover Image',
        }