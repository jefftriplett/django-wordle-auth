from django.test import override_settings

from djangowordleauth import checks


def test_fail_in_settings():
    errors = checks.check_config()
    assert len(errors) == 1
    assert errors[0].id == "dwa.E001"
    assert errors[0].msg == "Don't use django_wordle_auth in production"


@override_settings(
    AUTHENTICATION_BACKENDS=["django.contrib.auth.backends.ModelBackend"]
)
def test_success_not_in_settings():
    errors = checks.check_config()
    assert errors == []
