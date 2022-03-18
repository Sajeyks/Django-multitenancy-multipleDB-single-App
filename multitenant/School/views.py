from django.shortcuts import render
from .models import Student
# Create your views here.

def get_Students(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'index.html', context)