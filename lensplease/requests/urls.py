from django.conf.urls import patterns, url
from requests.views import PhotographerRequestAdd, PhotographerRequestUpdate, PhotographerRequestDelete

urlpatterns = patterns('',
    url(r'add/$', PhotographerRequestAdd.as_view(), name='photographerrequest_add'),
    url(r'(?P<pk>\d+)/$', PhotographerRequestUpdate.as_view(), name='photographerrequest_update'),
    url(r'(?P<pk>\d+)/delete/$', PhotographerRequestDelete.as_view(), name='photographerrequest_delete'),
)