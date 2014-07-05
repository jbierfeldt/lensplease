from django.forms import ModelForm
from django import forms
from landing.models import EmailSignup

class EmailSignupForm(ModelForm):
	class Meta:
		model = EmailSignup
		fields = ['email']
		
	def clean_email(self):
		email = self.cleaned_data['email']
		if EmailSignup.objects.filter(email=email).exists():
			raise forms.ValidationError(u'Email address already registered')
		return email