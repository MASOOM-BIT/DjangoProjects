from django import forms

class UserRegistrationForm(forms.Form):
    firstName = forms.CharField(max_length=100, label='First Name')
    lastName = forms.CharField(max_length=100, label='Last Name')
    email = forms.EmailField(label='Email')


# CSRF : cross site request forgery {% csrf_token %}

# form.as_p
# form.as_table
# form.as_ul