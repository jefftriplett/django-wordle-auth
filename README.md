# Django Wordle Auth

Django Wordle Auth is built for demo websites and should *never* be used in production.

Django Wordle Auth uses "today's Wordle" word of the day as your password.

## Install

```shell
python -m pip install django-wordle-auth
```

Then add `django_wordle_auth.backends.DjangoWordleAuthBackend` to your `settings.AUTHENTICATION_BACKENDS` like:

```python
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "django_wordle_auth.backends.DjangoWordleAuthBackend",
]
```
