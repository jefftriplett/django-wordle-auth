from typing import Any
from django.conf import settings
from django.core.checks import Error


def check_config(**kwargs: Any) -> list[Error]:
    errors = []

    if (
        "django_wordle_auth.backends.DjangoWordleAuthBackend"
        in settings.AUTHENTICATION_BACKENDS
    ):
        errors.extend(
            [
                Error(
                    "Don't use django_wordle_auth in production",
                    hint="Remove `DjangoWordleAuthBackend` from `settings.AUTHENTICATION_BACKENDS`",
                    id="dwa.E001",
                )
            ]
        )
    return errors
