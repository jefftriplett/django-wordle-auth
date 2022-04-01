from django.conf import settings


def pytest_configure():
    settings.configure(
        AUTHENTICATION_BACKENDS=[
            "django.contrib.auth.backends.ModelBackend",
            "django_wordle_auth.backends.DjangoWordleAuthBackend",
        ],
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": ":memory:",
            }
        },
        INSTALLED_APPS=[
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
        ],
        SECRET_KEY="testing-testing-testing",
        TIME_ZONE="UTC",
    )
