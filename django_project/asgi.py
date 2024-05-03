"""
ASGI config for djangoproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.routing import ChannelNameRouter, ProtocolTypeRouter
from django.core.asgi import get_asgi_application

from an_organ import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

chromatography_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": chromatography_asgi_app,
        "channel": ChannelNameRouter(
            {
                "instruments-add": consumers.SimpleInstrumentConsumer.as_asgi(),
            }
        ),
    }
)
