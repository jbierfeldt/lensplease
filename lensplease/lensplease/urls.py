from django.conf.urls import patterns, include, url

from landing.views import LandingView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', LandingView.as_view(), name='landing'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^requests/', include('requests.urls')),
)
