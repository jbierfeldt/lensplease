from django.shortcuts import render_to_response
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from requests.forms import PhotographerRequestForm

from requests.models import PhotographerRequest
        
class PhotographerRequestUpdate(UpdateView):
    model = PhotographerRequest
    success_url = "/"
    
class PhotographerRequestDelete(DeleteView):
    model = PhotographerRequest
    success_url = "/"
        

