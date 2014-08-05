from django.conf.urls import patterns, url
from photographer.forms import LandingPhotographerRegistrationForm
from registration.backends.default.views import RegistrationView

urlpatterns = patterns('',
    url(r'^register/$', RegistrationView.as_view(form_class=LandingPhotographerRegistrationForm, template_name="landing/photographerregistration_form.html"), name='photographer_register'),
)