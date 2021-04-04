from djongo import models

from .managers import UserManager


class User(models.Model):

    _id = models.ObjectIdField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    objects = UserManager()
