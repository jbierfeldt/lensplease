from django.db import models
from django.contrib.auth.models import User

class TimeStampedModel(models.Model):
     created_on = models.DateTimeField(auto_now_add=True)
     modified_on = models.DateTimeField(auto_now=True)

     class Meta:
         abstract = True
         
class PhotographerProfile(TimeStampedModel):
    """
    Custom user class for Photographers
    """
    user = models.ForeignKey(User, unique=True)
    first_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256, blank=True)
    age = models.IntegerField(max_length=2, blank=True, null=True)
    location = models.CharField(max_length=256)
    affiliation = models.CharField("College/University", max_length=256)
    
    
    def __unicode__(self):
        return self.user.username
        
    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('photographer_profile_detail', args=[self.user.username])