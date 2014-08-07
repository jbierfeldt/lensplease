from django.shortcuts import render_to_response
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse
from requests.forms import LandingPhotographerRequestForm
from django.contrib.messages.views import SuccessMessageMixin

from requests.models import PhotographerRequest

class PhotographerRequestCreate(SuccessMessageMixin, CreateView):

    template_name = 'requests/requests_add.html'
    form_class = LandingPhotographerRequestForm
    success_message = "Thanks, %(first_name)s! We'll contact you at %(email)s when we have news for you."
        
    def form_valid(self, form, **kwargs):
        form.save(commit = True)
        return super(PhotographerRequestCreate, self).form_valid(form)
        
    def get_success_url(self):
        return reverse('landing')
        
class PhotographerRequestUpdate(UpdateView):
    model = PhotographerRequest
    success_url = "/"
    
class PhotographerRequestDelete(DeleteView):
    model = PhotographerRequest
    success_url = "/"
        

