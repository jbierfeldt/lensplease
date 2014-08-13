from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

from photographer.forms import LandingPhotographerRegistrationForm
from photographer.views import PhotographerProfileUpdateView, PhotographerProfileDetailView

from photos.views import PortfolioPhotoCreate

urlpatterns = patterns('',
    url(r'^(?P<photographer_username>\w+)/$', PhotographerProfileDetailView.as_view(), name='photographer_profile_detail'),
    url(r'^(?P<photographer_username>\w+)/update/$', login_required(PhotographerProfileUpdateView.as_view()), name='photographer_profile_update'),
    url(r'^(?P<photographer_username>\w+)/update/photos/$', login_required(PortfolioPhotoCreate.as_view()), name='photographer_profile_photos_create'),
)