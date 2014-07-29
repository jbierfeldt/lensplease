from django.forms import ModelForm
from requests.models import PhotographerRequest

class PhotographerRequestForm(ModelForm):
    class Meta:
        model = PhotographerRequest
        fields = ['name', 'email', 'organization', 'max_price', 'date_needed', 'message']