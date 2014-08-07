from registration.signals import user_registered
from photographer.views import PhotographerRegistrationView
from photographer.models import PhotographerProfile
from django.contrib.auth.models import User

def createPhotographerProfile(sender, request, **kwargs):
    print "working!"
    profile = PhotographerProfile()
    profile.user = kwargs["user"]
    profile.location = request.POST["location"]
    profile.affiliation = request.POST["affiliation"]
    profile.save()

user_registered.connect(createPhotographerProfile, sender=PhotographerRegistrationView)