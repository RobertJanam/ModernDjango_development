from django.shortcuts import render
from .models import Book
from .forms import BookForm
from django.http import HttpResponse

# Create your views here.
def book(request, id):
    book = Book.objects.get(id=id)
    context = {"book": book}

    return render(request, 'book.html', context)

def books(request):
    books = Book.objects.all()
    context = {"books": books}

    return render(request, 'books.html', context)

def getbook(request):
    form = BookForm()
    context = {'form': form}

    return render(request, 'bookform.html', context)

def addbook(request):
    # check if request contains POST method
    if request.method == 'POST':
        form = BookForm(request.POST)
        # validate the form
        if form.is_valid():
            # extract the validated values of each field
            data = form.cleaned_data
            
            ttl = data['title']
            auth = data['author']
            pr = data['price']
            pu = data['publisher']
            
            b1 = Book(title=ttl, author=auth, price=pr, publisher=pu)
            b1.save()
            return HttpResponse('<h2 style="color: green;"> Book Added Successfully ✅</h2>')    
            
def test(request):
    return HttpResponse("<h2>Hello</h2>")