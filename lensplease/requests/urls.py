from django.conf.urls import patterns, url
from requests.views import PhotographerRequestCreate

urlpatterns = patterns('',
    url(r'^add/$', PhotographerRequestCreate.as_view(), name='photographerrequest_create'),
    #url(r'(?P<pk>\d+)/$', PhotographerRequestUpdate.as_view(), name='photographerrequest_update'),
    #url(r'(?P<pk>\d+)/delete/$', PhotographerRequestDelete.as_view(), name='photographerrequest_delete'),
)