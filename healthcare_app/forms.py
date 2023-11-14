from django import forms
from .models import Person, Referral


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'phone_number', 'date_of_birth']
               
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}, format='%Y-%m-%d'),
        }


class ReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ['referral_date', 'referrer_name', 'referral_reason', 'note', 'document']
        
        widgets = {
            'referral_date': forms.DateInput(attrs={'class': 'form-control'}),
            'referrer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'referral_reason': forms.Textarea(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control'}),
        }