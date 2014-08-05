from registration.signals import user_registered
from registration.backends.default.views import RegistrationView
from django.core.signals import request_finished
from photographer.models import PhotographerProfile
from django.contrib.auth.models import User

def createPhotographerProfile(sender, request, **kwargs):
    profile = PhotographerProfile()
    profile.user = kwargs["user"]
    profile.location = request.POST["location"]
    profile.affiliation = request.POST["affiliation"]
    profile.save()

user_registered.connect(createPhotographerProfile, sender=RegistrationView)