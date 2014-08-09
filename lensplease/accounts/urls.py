from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

from photographer.forms import LandingPhotographerRegistrationForm
from photographer.views import PhotographerRegistrationView, PhotographerActivationView


urlpatterns = patterns('',
    url(r'^photographer/register/$', PhotographerRegistrationView.as_view(form_class=LandingPhotographerRegistrationForm), name='photographer_register'),
    url(r'^photographer/register/complete/$', TemplateView.as_view(template_name='photographer/registration_complete.html'), name='photographerregistration_complete'),
    url(r'^photographer/activate/(?P<activation_key>\w+)/$', PhotographerActivationView.as_view(), name='photographerregistration_activate'),
    url(r'^photographer/activation/complete/$', TemplateView.as_view(template_name='photographer/activation_complete.html'), name='photographer_activation_complete'),
    url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html'}, name='account_login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'accounts/logout.html', 'next_page': 'landing'}, name='account_logout'),
    (r'', include('registration.auth_urls')),
)