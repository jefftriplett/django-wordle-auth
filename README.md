# Django Wordle Auth

Django Wordle Auth backend that uses today's Wordle word of the day as your password.

:fire: Django Wordle Auth is built for demo websites and **should never be used in a production environment**. :fire: 

Words are hashed to prevent spoilers.

Writing the tests and hasing the words were the most fun aspects of this project. 

## Install

```shell
# If this project were on PyPi
python -m pip install django-wordle-auth

# TODO... Install from the repo...
```

Then add `django_wordle_auth.backends.DjangoWordleAuthBackend` to your `settings.AUTHENTICATION_BACKENDS` like:

```python
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "django_wordle_auth.backends.DjangoWordleAuthBackend",
]
```

## Legal 

- Django Wordle Auth is not associated with the Django Software Foundation or The New York Times Company.
- Django is a registered trademark of the Django Software Foundation.
- I suspect Wordle is or is soon to be a registered trademark of The New York Times Company.
