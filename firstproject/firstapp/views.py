from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("<h3> Know more about FirstApp. </h3>")

def user(request, name):
    return HttpResponse(f"<h2> Hello, {name}. Welcome to FirstApp Home Page.")