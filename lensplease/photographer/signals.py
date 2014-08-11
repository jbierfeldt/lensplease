from registration.signals import user_registered, user_activated
from photographer.views import PhotographerRegistrationView
from photographer.models import PhotographerProfile
from django.contrib.auth.models import User
from django.contrib.auth import login

def createPhotographerProfile(sender, request, **kwargs):
    profile = PhotographerProfile()
    profile.user = kwargs["user"]
    profile.location = request.POST["location"]
    profile.affiliation = request.POST["affiliation"]
    profile.save()
    
user_registered.connect(createPhotographerProfile, sender=PhotographerRegistrationView)


def login_on_activation(sender, user, request, **kwargs):
    user.backend='django.contrib.auth.backends.ModelBackend' 
    login(request,user)
    
user_activated.connect(login_on_activation)