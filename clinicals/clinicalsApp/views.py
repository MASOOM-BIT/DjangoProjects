from django.shortcuts import render
from clinicalsApp.models import Patient
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy 
# Create your views here.

class PatientListView(ListView):
    model = Patient
    #template_name = 'clinicalsApp/patient_list.html'

class PatientCreateView(CreateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('firstName', 'lastName', 'age')
    #template_name = 'clinicalsApp/patient_form.html'

class PatientUpdateView(UpdateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('firstName', 'lastName', 'age')
    #template_name = 'clinicalsApp/patient_form.html'

class PatientDeleteView(DeleteView):
    model= Patient
    success_url = reverse_lazy('index')
    #template_name = 'clinicalsApp/patient_confirm_delete.html'

