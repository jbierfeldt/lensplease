from django import forms
from django.forms import ModelForm
from requests.models import PhotographerRequest

class PhotographerRequestForm(ModelForm):
    class Meta:
        model = PhotographerRequest
        fields = ['first_name', 'last_name', 'email', 'organization', 'max_price', 'date_needed', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'organization': forms.TextInput(attrs={'placeholder': 'Organization (optional)', 'class': 'form-control'}),
            'max_price': forms.TextInput(attrs={'data-slider-id=': 'id_max_priceSlider', 'data-slider-min': 10, 'data-slider-max': 200, 'data-slider-step': 1, 'data-slider-value': 25, 'type': 'range'}),
            'date_needed': forms.DateInput(attrs={'placeholder': 'mm/dd/yyyy', 'class': 'form-control', 'type': 'date'}),
            'message': forms.Textarea(attrs={'placeholder': 'Howdy! I\'m looking for...', 'class': 'form-control'}),
        }