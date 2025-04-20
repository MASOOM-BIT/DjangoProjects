from django.shortcuts import render
from formsApp import forms
# Create your views here.

def userRegistrationView(request):
    form = forms.UserRegistrationForm()
    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            print("User Registration Successful")
            print("First Name :", form.cleaned_data['firstName'])
            print("Last Name :", form.cleaned_data['lastName'])
            print("Email :", form.cleaned_data['email'])
            
    return render (request, 'formsApp/userRegistration.html', {'form': form})
