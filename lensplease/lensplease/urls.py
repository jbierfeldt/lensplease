from django.conf.urls import patterns, include, url

from landing.views import landing

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', landing, name='landing'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
)
