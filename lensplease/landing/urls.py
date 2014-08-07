from django.conf.urls import patterns, url
from landing.views import LandingView

urlpatterns = patterns('',
    url(r'^$', LandingView.as_view(), {}, name='landing'),
)