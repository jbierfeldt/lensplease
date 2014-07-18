"""
settngs/development.py
Development settings for lensplease.

The development environment is light and local. All data is stored underneath
the development virtualenv.
"""
import os

from .common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "lensplease",
        "USER": "",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "",
    }
}

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'testing@example.com'

INSTALLED_APPS += ("debug_toolbar", )
INTERNAL_IPS = ("127.0.0.1",)
MIDDLEWARE_CLASSES += ("debug_toolbar.middleware.DebugToolbarMiddleware", )
SECRET_KEY = 's'

if 'LENSPLEASE_CONFIG_PATH' in os.environ:
    execfile(os.environ['LENSPLEASE_CONFIG_PATH'])
