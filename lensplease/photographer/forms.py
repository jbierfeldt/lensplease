from django import forms

from registration.forms import RegistrationForm
    
from photographer.models import PhotographerProfile

class LandingPhotographerRegistrationForm(RegistrationForm):
    def __init__(self, *args, **kwargs):
        super(LandingPhotographerRegistrationForm,self).__init__(*args, **kwargs)
    
    common_attrs_dict = {'class': 'form-control'}
    
    username = forms.RegexField(regex=r'^\w+$', max_length=30, widget=forms.TextInput(attrs=dict(common_attrs_dict, placeholder="Username")), label="Username", error_messages={'invalid': "This value must contain only letters, numbers and underscores."})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(common_attrs_dict, placeholder="Email")), label="Email address")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(common_attrs_dict, placeholder="Password"), render_value=False), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(common_attrs_dict, placeholder="Password (again)"), render_value=False), label="Password (again)")
    location = forms.CharField(widget=forms.TextInput(attrs=dict(common_attrs_dict, placeholder="Location")))
    affiliation = forms.CharField(widget=forms.TextInput(attrs=dict(common_attrs_dict, placeholder="College/University")))
    
class PhotographerProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = PhotographerProfile
        exclude = ('user',)
        common_attrs_dict = {'class': 'form-control'}
        widgets = {
            'first_name': forms.TextInput(attrs=common_attrs_dict),
            'last_name': forms.TextInput(attrs=common_attrs_dict),
            'age': forms.NumberInput(attrs=common_attrs_dict),
            'location': forms.TextInput(attrs=common_attrs_dict),
            'affiliation': forms.TextInput(attrs=common_attrs_dict),
            'price_range': forms.TextInput(attrs=common_attrs_dict),
            'specialties': forms.TextInput(attrs=common_attrs_dict),
            'short_description': forms.Textarea(attrs=dict(common_attrs_dict, rows=3)),
            'bio': forms.Textarea(attrs=dict(common_attrs_dict, rows=6)),
            'camera': forms.TextInput(attrs=common_attrs_dict),
            'other_equipment': forms.TextInput(attrs=common_attrs_dict),
            'editing': forms.TextInput(attrs=common_attrs_dict),
        }