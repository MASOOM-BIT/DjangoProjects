from django import forms
from django.core import validators


class UserRegistrationForm(forms.Form):
    GENDER = [{'male','MALE'},{'female','FEMALE'}]
    firstName = forms.CharField(max_length=100, label='First Name', validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(20)])
    lastName = forms.CharField(max_length=100, label='Last Name')
    email = forms.EmailField(label='Email',required=False)
    gender=forms.CharField(widget=forms.Select(choices=GENDER))
    password = forms.CharField(widget=forms.PasswordInput())


'''
def clean_firstName(self):
    inputFirstName = self.cleaned_data['firstName']
    if len(inputFirstName) > 20:
        raise forms.ValidationError("The max length of first name is 20 characters")
    return inputFirstName


def clean_email(self):
    inputEmail = self.cleaned_data['email']
    if inputEmail.find('@') == -1:
        raise forms.ValidationError("Email should contain @")
    return inputEmail

# -------------single clean function-----
def clean(self):
    cleaned_data = super().clean()
    inputFirstName = cleaned_data.get('firstName')
    inputEmail = cleaned_data.get('email')
    
    if len(inputFirstName) > 20:
        self.add_error('firstName', "The max length of first name is 20 characters")
    
    if inputEmail and inputEmail.find('@') == -1:
        self.add_error('email', "Email should contain @")
    
    return cleaned_data
    '''
# CSRF : cross site request forgery {% csrf_token %}

# form.as_p
# form.as_table
# form.as_ul