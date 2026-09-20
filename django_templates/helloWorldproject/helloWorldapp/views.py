from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request, name):
    return HttpResponse('<h2>Hello, {name}</h2>'.format(name=name))

def index(request, name):
    context = {'name': name}
    return render(request, 'index.html', context)

def marks(request):
    marks = [78, 76, 79]
    context = {'marks': marks}
    return render(request, 'marks.html', context)