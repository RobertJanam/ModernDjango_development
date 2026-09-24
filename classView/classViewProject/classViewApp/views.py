from django.shortcuts import render
#from django.urls import reverse # use this if you intend to define get_success_url method
from django.urls import reverse_lazy # access a url (kinda like a redirect)
from django.views import View # better control and flexibility
from .forms import BookForm
from django.http import HttpResponse
from django.views.generic.base import TemplateView # TemplateView is defined in this class
from django.views.generic import CreateView # Importing CreateView from generic module
from .models import Book # importing Book Model

# Create your views here.
def addbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('<h2 style="color: green;"> Book Added Successfully ✅</h2>')
    else:
        form = BookForm()

    return render(request, 'bookform.html', {'form': form})

class MyView(View):
    def get(self, request): # define get method to render html page
        return render(request, 'name.html', {})
    
    def post(self, request):
        name = request.POST['name'] #fetch the name
        return HttpResponse(f"<h2>Hello, {name}</h2>")
    
def displaybook(request):
    books = Book.objects.all()
    
    context = {"books": books}
    
    return render(request, 'getbooks.html', context)

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        # context = {'name': 'John'} # uncomment to test it out. Comment the immediate line below first. Also, remember to update urls first.
        context = {'name': self.kwargs['name']}
        
        return context

class CreateBookView(CreateView):
    model = Book # uses the Book model
    fields = ['title', 'author', 'price', 'publisher', 'ebook']
    
    template_name = "bookform.html" # get the html file
    
    success_url = reverse_lazy('getbooks') # redirect to this URL
    
    # def get_success_url(self): # same as this above
    #     return reverse('getbooks') # use this instead of reverse_lazy
    