import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from passlib.context import CryptContext


def _create_hash():
    password_context = CryptContext(schemes=["bcrypt"],
                                    deprecated="auto")
    return password_context.hash


class User(AbstractUser):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    username = models.CharField(max_length=100, unique=True, blank=False)
    password = models.CharField(max_length=24,
                                default=_create_hash,
                                blank=False)

    USERNAME_FIELD = "username"


# Create your models here.
