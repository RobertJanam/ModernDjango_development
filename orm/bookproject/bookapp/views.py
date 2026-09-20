from django.shortcuts import render
from .models import Book
from .forms import BookForm
from django.http import HttpResponse

# Create your views here.
# get some book (requires id to be added to the path parameter)
def book(request, id):
    book = Book.objects.get(id=id) # gets the id number provided in the URL
    context = {"book": book} # Acts as a placeholder for the template file

    return render(request, 'book.html', context)

# get all books
def books(request):
    books = Book.objects.all()
    context = {"books": books}

    return render(request, 'books.html', context)

# add book using a form manually (very trash)
def getbook(request):
    form = BookForm() # retrieves the BookForm class.
    context = {'form': form}

    return render(request, 'bookform.html', context)

# add book using a form
def addbook(request):
    # check if request contains POST method
    if request.method == 'POST':
        form = BookForm(request.POST)
        # validate the form
        if form.is_valid():
            # extract the validated values of each field
            #data = form.cleaned_data
            #ttl = data['title']
            #auth = data['author']
            #pr = data['price']
            #pu = data['publisher'] 
            #b1 = Book(title=ttl, author=auth, price=pr, publisher=pu)
            #b1.save()
            
            #here's a simpler and much more convinient way.
            form.save() # this is because we already set the model attribute in form class
            return HttpResponse('<h2 style="color: green;"> Book Added Successfully ✅</h2>')    
            
# update a book (author is required as part of the path parameter)
def updatebook(request, author):
    book = Book.objects.get(author=author)
    form = BookForm(instance=book) # specify the instance attribute in the constructor
    context = {'form': form}
    
    return render(request, 'bookform.html', context)

def test(request):
    return HttpResponse("<h2>Hello</h2>")