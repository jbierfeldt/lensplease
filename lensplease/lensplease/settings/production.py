"""
settngs/production.py
Production settings for lensplease.
"""

import os

from .common import *

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
    '.lensplease.com', # Allow domain and subdomains
    '.lensplease.com.', # Also allow FQDN and subdomains
    '.shutterclub.co',
    '.shutterclub.co.',
	]
	
DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'lensplease',
                'USER': 'lensplease',
                'PASSWORD': os.environ["PROD_DB_PASS"],
                'HOST': 'localhost',
                'PORT': '',
            }
        }
        
SECRET_KEY = os.environ["PROD_SECRET_KEY"]

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = "shutterclub.io@gmail.com"
EMAIL_HOST_PASSWORD = os.environ["GMAIL_PASS"]
DEFAULT_FROM_EMAIL = 'shutterclub.io@gmail.com'