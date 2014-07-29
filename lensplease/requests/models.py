from django.db import models
from django import forms
from django.core.urlresolvers import reverse


class TimeStampedModel(models.Model):
     created_on = models.DateTimeField(auto_now_add=True)

     class Meta:
         abstract = True
         
class PhotographerRequest(TimeStampedModel):
    name = models.CharField(max_length=256, verbose_name="Name")
    email = models.EmailField(max_length=256)
    organization = models.CharField(max_length=256, blank=True)
    max_price = models.IntegerField(verbose_name="I'm looking to spend no more than...")
    date_needed = models.DateField()
    message = models.TextField()
    
    satisfied = models.BooleanField(default=False)
    
    def __unicode__(self):
		return str("Request from" + " " + self.name + " " + "for less than" + " $" + str(self.max_price))
        
