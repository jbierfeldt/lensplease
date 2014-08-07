from registration.backends.default.views import RegistrationView, ActivationView

class PhotographerRegistrationView(RegistrationView):

    template_name="photographer/registration_form.html"
    
    def form_valid(self, request, form):
        return super(PhotographerRegistrationView, self).form_valid(request, form)
        
    
    def get_success_url(self, request, user):
        """
        Return the name of the URL to redirect to after successful
        user registration.
        
        """
        return ('photographerregistration_complete', (), {})
    
        
class PhotographerActivationView(ActivationView):

    template_name = 'photographer/activate.html'
    
    def get_success_url(self, request, user):
        return ('photographer_profile_detail', (), {"photographer_username": user.username})