from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms

from landing.models import EmailSignup
from landing.forms import EmailSignupForm


def landing(request):
	if request.method == 'POST':
		form = EmailSignupForm(request.POST)
		if form.is_valid():
			submitted_email = form.cleaned_data['email']
			
			e = EmailSignup()
			e.email = submitted_email
			e.save()
			
			return render_to_response('landing/landing.html', {"email_success": submitted_email, "e": e}, context_instance=RequestContext(request))
			
	else:
		form = EmailSignupForm()
		
	return render_to_response('landing/landing.html', {"form": form}, context_instance=RequestContext(request))

# Create your views here.
