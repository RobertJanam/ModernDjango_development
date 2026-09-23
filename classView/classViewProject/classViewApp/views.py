from django.shortcuts import render
from django.views import View # better control and flexibility
from .forms import BookForm
from django.http import HttpResponse
from django.views.generic.base import TemplateView # TemplateView is defined in this class

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
    def get(self, request):
        return render(request, 'name.html', {})
    
    def post(self, request):
        name = request.POST['name']
        return HttpResponse(f"<h2>Hello, {name}</h2>")
    
class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        # context = {'name': 'John'} # uncomment to test it out. Comment the immediate line below first. Also, remember to update urls first.
        context = {'name': self.kwargs['name']}
        
        return context
