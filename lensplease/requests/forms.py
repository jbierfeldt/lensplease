from django import forms
from django.forms import ModelForm
from requests.models import PhotographerRequest

class SliderWidget(forms.TextInput):
    input_type = 'range'
    
    def __init__(self, attrs=None):
        super(SliderWidget, self).__init__(attrs)
        
    def render(self, name, value, attrs=None):
        if value:
            value = value
        attrs["data-slider-value"] = value
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        return super(SliderWidget, self).render(name, value, final_attrs)
        
        
class LandingPhotographerRequestForm(ModelForm):
    class Meta:
        model = PhotographerRequest
        fields = ['first_name', 'last_name', 'email', 'city', 'phone', 'organization', 'max_price', 'date_needed', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'city': forms.TextInput(attrs={'placeholder': 'City', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control bfh-phone', 'data-country': 'US'}),
            'organization': forms.TextInput(attrs={'placeholder': 'Organization (optional)', 'class': 'form-control'}),
            'max_price': SliderWidget(attrs={'data-slider-id': 'id_max_priceSlider', 'data-slider-min': 10, 'data-slider-max': 200, 'data-slider-step': 1}),
            'date_needed': forms.DateInput(attrs={'placeholder': 'mm/dd/yyyy', 'class': 'form-control', 'type': 'date'}),
            'message': forms.Textarea(attrs={'placeholder': 'Howdy! I\'m looking for...', 'class': 'form-control', 'rows':4}),
        }