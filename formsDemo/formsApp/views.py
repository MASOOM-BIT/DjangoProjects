from django.shortcuts import render
from formsApp import forms
# Create your views here.

def userRegistrationView(request):
    form = forms.UserRegistrationForm()
    
    if request.method == 'POST':
        print("Form submitted")  # confirm POST is working
        form = forms.UserRegistrationForm(request.POST)
        
        if form.is_valid():
            print("Form is valid")
            print("User Registration Successful")
            print("First Name:", form.cleaned_data['firstName'])
            print("Last Name:", form.cleaned_data['lastName'])
            print("Email:", form.cleaned_data['email'])
        else:
            print("Form is invalid")
            print(form.errors)
    
    return render(request, 'formsApp/userRegistration.html', {'form': form})