from django.conf.urls import patterns, url
from photographer.forms import LandingPhotographerRegistrationForm
from django.views.generic.base import TemplateView
from photographer.views import PhotographerProfileUpdateView, PhotographerProfileDetailView, PhotographerRegistrationView, PhotographerActivationView

urlpatterns = patterns('',
    url(r'^registration/register/$', PhotographerRegistrationView.as_view(form_class=LandingPhotographerRegistrationForm), name='photographer_register'),
    url(r'^registration/complete/$', TemplateView.as_view(template_name='photographer/registration_complete.html'), name='photographerregistration_complete'),
    url(r'^registration/activate/(?P<activation_key>\w+)/$', PhotographerActivationView.as_view(), name='photographerregistration_activate'),
    url(r'^registration/activation/complete/$', TemplateView.as_view(template_name='photographer/activation_complete.html'), name='photographer_activation_complete'),
    url(r'^(?P<photographer_username>\w+)/$', PhotographerProfileDetailView.as_view(), name='photographer_profile_detail'),
    url(r'^(?P<photographer_username>\w+)/update/$', PhotographerProfileUpdateView.as_view(), name='photographer_profile_update'),
)