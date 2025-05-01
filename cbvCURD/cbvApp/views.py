from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from cbvApp.models import Student
# Create your views here.

class StudentListView(ListView):
    model=Student


    #default template_name is student_list.html
    # template_name = 'student_list.html'
    # default context_object_name = 'student_list'

class StudentDetailView(DetailView):
    model=Student
    # default template_name is student_detail.html
    # template_name = 'student_detail.html'
    # default context_object_name = 'student'

class StudentCreateView(CreateView):
    model=Student
    fields=['firstName','lastName','testScore']
    # template_name = 'student_form.html'