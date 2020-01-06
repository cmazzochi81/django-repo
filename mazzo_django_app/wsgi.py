"""
WSGI is how the python application and web server communicate.
WSGI config for mazzo_django_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mazzo_django_app.settings')

application = get_wsgi_application()
