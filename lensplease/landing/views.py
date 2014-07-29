from django.views.generic.base import TemplateView
from requests.forms import PhotographerRequestForm

class LandingView(TemplateView):

    template_name = "landing/landing.html"

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)
        context['photographerrequest_form'] = PhotographerRequestForm
        return context
