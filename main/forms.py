from django import forms
from .models import Enquiry

class EnquiryForm(forms.ModelForm):
    class Meta:
        model  = Enquiry
        fields = ['name', 'company', 'phone', 'email', 'product', 'message']
        widgets = {
            'name':    forms.TextInput(attrs={'placeholder': 'e.g. Rajesh Sharma', 'class': 'form-control'}),
            'company': forms.TextInput(attrs={'placeholder': 'e.g. ABC Quarry Pvt Ltd', 'class': 'form-control'}),
            'phone':   forms.TextInput(attrs={'placeholder': '+91 98765 43210', 'class': 'form-control'}),
            'email':   forms.EmailInput(attrs={'placeholder': 'your@email.com', 'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-select'}),
            'message': forms.Textarea(attrs={
                'placeholder': 'Screen size, aperture size, wire diameter, quantity, application...',
                'class': 'form-control', 'rows': 4
            }),
        }
