from django.shortcuts import render
from django.views import View # better control and flexibility
from django.http import HttpResponse

# Create your views here.
class MyView(View):
    def get(self, request):
        return render(request, 'index.html', {})
    
    def post(self, request):
        name = request.POST['name']
        return HttpResponse(f"<h2>Hello, {name}</h2>")