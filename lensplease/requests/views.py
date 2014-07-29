from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from requests.models import PhotographerRequest

class PhotographerRequestCreate(CreateView):
    model = PhotographerRequest
    success_url = "/"
        
class PhotographerRequestUpdate(UpdateView):
    model = PhotographerRequest
    success_url = "/"
    
class PhotographerRequestDelete(DeleteView):
    model = PhotographerRequest
    success_url = "/"
        

