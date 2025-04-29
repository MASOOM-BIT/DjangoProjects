from django.shortcuts import render
from django.views.generic import ListView
from cbvApp.models import Student
# Create your views here.

class StudentListView(ListView):
    model=Student


    #default template_name is student_list.html
    # template_name = 'student_list.html'
    # default context_object_name = 'student_list'