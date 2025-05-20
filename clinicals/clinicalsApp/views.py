from django.shortcuts import render,redirect
from clinicalsApp.models import Patient,ClinicalData
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from clinicalsApp.forms import ClinicalDataForm
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

def addData(request,**kwargs):
    form = ClinicalDataForm()
    patient = Patient.objects.get(id=kwargs['pk'])
    if request.method == 'POST':
        form = ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'clinicalsApp/clinicaldata_form.html',{'form':form,'patient':patient})


def analyze(request, **kwargs):
    data = ClinicalData.objects.filter(patient_id=kwargs['pk'])
    responseData = []

    for eachEntry in data:
        responseData.append(eachEntry)

        if eachEntry.componentName == 'hw':
            try:
                height_str, weight_str = eachEntry.componentValue.split('/')
                height_in_feet = float(height_str)
                weight_in_kg = float(weight_str)

                height_in_meters = height_in_feet * 0.3048
                if height_in_meters > 0:
                    bmi = weight_in_kg / (height_in_meters ** 2)
                    bmiEntry = ClinicalData()
                    bmiEntry.componentName = 'BMI'
                    bmiEntry.componentValue = f"{bmi:.2f}"  # format to 2 decimal places
                    responseData.append(bmiEntry)
            except (ValueError, ZeroDivisionError):
                # Handle invalid data formats gracefully
                continue

    return render(request, 'clinicalsApp/generateReport.html', {'data': responseData})

