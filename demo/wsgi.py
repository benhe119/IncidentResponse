"""
WSGI config for demo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from .actions.headline_actions import *
from .actions.incident_commands import *
from .actions.incident_notifications import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings.dev')

application = get_wsgi_application()
