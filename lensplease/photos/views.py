from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404

from photos.forms import PortfolioPhotoForm
from photographer.models import PhotographerProfile

class PortfolioPhotoCreate(SuccessMessageMixin, CreateView):

    template_name = 'photographer/photographerprofile_photo_form.html'
    form_class = PortfolioPhotoForm
    success_message = "Photo uploaded."
            
    def get_object(self, queryset=None):
        obj = PhotographerProfile.objects.get(user__username=self.kwargs['photographer_username'])
        return obj
    
    def get_initial(self):
        obj = self.get_object()
        if obj.user.id != self.request.user.id:
            raise Http404('You do not have permission to view this page')
        else:
            return super(PortfolioPhotoCreate, self).get_initial()
        
    def form_valid(self, form, **kwargs):
        form.instance.photographer_profile = self.get_object()
        return super(PortfolioPhotoCreate, self).form_valid(form)
        
    def get_success_url(self, **kwargs):
        return reverse('photographer_profile_update', kwargs = {'photographer_username': self.kwargs['photographer_username']})