from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from requests.forms import LandingPhotographerRequestForm
from photographer.forms import LandingPhotographerRegistrationForm

class LandingView(TemplateView):

    template_name = "landing/landing.html"

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)
        context['photographerrequest_form'] = LandingPhotographerRequestForm
        context['photographerregistration_form'] = LandingPhotographerRegistrationForm
        
        return context
        
class PhotographerRequestCreate(SuccessMessageMixin, CreateView):

    template_name = 'landing/landing.html'
    form_class = LandingPhotographerRequestForm
    success_message = "Thanks, %(first_name)s! We'll contact you at %(email)s when we have news for you."
    
    def get_context_data(self, **kwargs):
        context = super(PhotographerRequestCreate, self).get_context_data(**kwargs)
        context['photographerrequest_form'] = context.get('form')
        context['anchor'] = 'request-form'
        return context
        
    def get_success_url(self):
        return reverse('landing')
        
    def form_valid(self, form, **kwargs):
        form.save(commit = True)
        return super(PhotographerRequestCreate, self).form_valid(form)
