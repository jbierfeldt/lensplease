from registration.forms import RegistrationForm
from django import forms
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