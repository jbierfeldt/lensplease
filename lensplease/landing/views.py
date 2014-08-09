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