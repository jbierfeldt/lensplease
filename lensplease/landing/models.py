from django.db import models

class EmailSignup(models.Model):
	"""
	Information collected from people signing up for the waitlist
	
	"""
	email = models.EmailField(max_length=256)
	created_at = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return str(self.email)
