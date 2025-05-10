from django import forms

class ItemForm(forms.Form):
    name = forms.CharField(max_length=100, label='Item Name')
    quantity = forms.IntegerField(min_value=1, label='Quantity')