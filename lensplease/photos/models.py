from django.db import models

from photographer.models import PhotographerProfile

import cloudinary
from cloudinary.models import CloudinaryField

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^cloudinary\.models\.CloudinaryField"])

class TimeStampedModel(models.Model):
     created_on = models.DateTimeField(auto_now_add=True)
     modified_on = models.DateTimeField(auto_now=True)

     class Meta:
         abstract = True
         
class Photo(TimeStampedModel):
    title = models.CharField("Title (optional)", max_length=256, blank=True)
    
    image = CloudinaryField('image')
    
    def __unicode__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ''
        return "Photo <%s:%s>" % (self.title, public_id)
        
    class Meta:
        abstract = True
        
class PortfolioPhoto(Photo):
    photographer_profile = models.ForeignKey(PhotographerProfile)
    
    def __unicode__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ''
        return "Photo <%s:%s>" % (self.title, public_id)
