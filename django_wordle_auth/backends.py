import hashlib

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.utils.timezone import now

from django_wordle_auth.words import WORDS


UserModel = get_user_model()


class DjangoWordleAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if username is None or password is None:
            return
        try:
            user = UserModel._default_manager.get_by_natural_key(username)
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password(password)
        else:
            if self.user_can_authenticate(user):
                day = now().strftime("%Y-%m-%d")
                hashed_password = hashlib.md5(password.encode()).hexdigest()
                if day in WORDS and hashed_password == WORDS[day]:
                    return user
