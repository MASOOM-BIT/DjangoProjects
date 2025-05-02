from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from cbvApp.models import Student
from django.urls import reverse_lazy
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

class StudentUpdateView(UpdateView):
    model=Student
    fields=('testScore',)
    # template_name = 'student_form.html'

class StudentDeleteView(DeleteView):
    model=Student
    # template_name = 'student_confirm_delete.html'
    # default success_url = '/students/'
    success_url = reverse_lazy("StudentListView")