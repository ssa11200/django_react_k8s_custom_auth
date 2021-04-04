from django.contrib.auth.hashers import make_password
from djongo import models

# hash the password before storing in db
class UserManager(models.Manager):
    def create(self, **kwargs):
        return super().create(
            # override password key-value in dict
            **{**kwargs, "password": make_password(kwargs["password"])},
        )
