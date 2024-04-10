from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['patient_number', 'first_name', 'last_name', 'age', 'email', 'phone_number', 'has_paid', 'payment_method']
        labels = {
            'patient_number': 'Patient Number',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'has_paid': 'Has Paid',
            'payment_method': 'Payment Method'
        }
        widgets = {
            'patient_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}), 
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'has_paid': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'payment_method': forms.TextInput(attrs={'class': 'form-control'}),
        }