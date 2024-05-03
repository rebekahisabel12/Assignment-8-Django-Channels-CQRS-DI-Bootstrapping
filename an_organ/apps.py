from django.apps import AppConfig


class AnOrganConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'an_organ'

    def ready(self):
        import an_organ.signals
