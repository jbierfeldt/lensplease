from django.db import models
from django import forms
from django.core.urlresolvers import reverse


class TimeStampedModel(models.Model):
     created_on = models.DateTimeField(auto_now_add=True)
     modified_on = models.DateTimeField(auto_now=True)

     class Meta:
         abstract = True
         
class PhotographerRequest(TimeStampedModel):
    first_name = models.CharField(max_length=256, verbose_name="First Name")
    last_name = models.CharField(max_length=256, verbose_name="Last Name")
    email = models.EmailField(max_length=256)
    city = models.CharField(max_length=256)
    phone = models.CharField(max_length=20, verbose_name="Phone Number", blank=True)
    organization = models.CharField(max_length=256, blank=True)
    max_price = models.IntegerField(verbose_name="Max Price", default=50)
    date_needed = models.DateField(blank=True, null=True)
    message = models.TextField(blank=True)
    
    # Meta Fields
    follow_up = models.BooleanField(default=False, verbose_name="Followed up?")
    fulfilled = models.BooleanField(default=False, verbose_name="Fulfilled?")
    payment_received = models.BooleanField(default=False, verbose_name="Payment Received?")
    payment_made = models.BooleanField(default=False, verbose_name="Payment Made?")
    notes = models.TextField(blank=True, verbose_name="Notes for Administrators")
    
    # ForeignKey to Photographer Set Later
    
    def __unicode__(self):
		return str("Request from" + " " + self.first_name + " " + "for less than" + " $" + str(self.max_price))
        
