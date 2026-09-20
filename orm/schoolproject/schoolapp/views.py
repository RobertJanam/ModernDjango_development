from django.shortcuts import render
from .models import Teacher

# Create your views here.
def teachers(request):
    # get every teacher
    teachers = Teacher.objects.values('name', 'email', 'qualification', 'college')
    # context
    context = {"teachers": teachers}
    
    return render(request, 'teachers.html', context)