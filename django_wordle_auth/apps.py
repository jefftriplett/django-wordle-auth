from django.apps import AppConfig
from django.core.checks import register, Tags

from django_wordle_auth.checks import check_config


class DjangoWordleAuthConfig(AppConfig):
    name = "django_wordle_auth"
    verbose_name = "django-wordle-auth"

    def ready(self):
        register(Tags.security)(check_config)
