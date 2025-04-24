from django.shortcuts import render
from fbvApp.models import Student
# Create your views here.

def getStudents(request):
    students = Student.objects.all()
    return render(request, 'fbvApp/index.html', {'students': students})