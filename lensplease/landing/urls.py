from django.conf.urls import patterns, url
from landing.views import PhotographerRequestCreate, LandingView

urlpatterns = patterns('',
    url(r'^$', LandingView.as_view(), {}, name='landing'),
    url(r'^add/$', PhotographerRequestCreate.as_view(), name='photographerrequest_create'),
)