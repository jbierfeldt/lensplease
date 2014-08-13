from django import forms

from cloudinary.forms import CloudinaryFileField

from photos.models import PortfolioPhoto

class PortfolioPhotoForm(forms.ModelForm):
    class Meta:
        model = PortfolioPhoto
        exclude = ('photographer_profile',)
        common_attrs_dict = {'class': 'form-control'}
        widgets = {
            'title': forms.TextInput(attrs=common_attrs_dict),
            'image': forms.ClearableFileInput(attrs=common_attrs_dict),
        }