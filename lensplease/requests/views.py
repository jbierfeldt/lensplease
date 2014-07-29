from django.shortcuts import render_to_response
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from requests.forms import PhotographerRequestForm

from requests.models import PhotographerRequest

class PhotographerRequestAdd(FormView):
    template_name = 'landing/landing.html'
    form_class = PhotographerRequestForm
    success_url = "/"
    
    def get_context_data(self, **kwargs):
        context = super(PhotographerRequestAdd, self).get_context_data(**kwargs)
        context['photographerrequest_form'] = context.get('form')
        return context
        
class PhotographerRequestUpdate(UpdateView):
    model = PhotographerRequest
    success_url = "/"
    
class PhotographerRequestDelete(DeleteView):
    model = PhotographerRequest
    success_url = "/"
        

