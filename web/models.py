from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.core.exceptions import PermissionDenied




# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, username, name ,email, password=None):
        if not email:
            raise ValueError('Users should have an email address')

        user = self.model(
            username=username,
            name = name,
            email = self.normalize_email(email),
            joined_at=timezone.now()
        )


        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, username, name, email, password):
        user = self.create_user(
            username,
            name,
            email, 
            password
        )


        user.is_staff = True
        user.is_admin = True
        user.save()

        return user

    
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=10,unique=True)
    email = models.EmailField(max_length=40, unique=True)
    joined_at = models.DateTimeField(default=timezone.now) 
    avatar = models.ImageField(upload_to='upload/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["email", "name"]

    def __str__(self):
        return "@{}".format(self.username)

    def get_short_name(self):
        return self.name

    def get_long_name(self):
        return "{} (@{})".format(self.name, self.username)

    @property
    def is_superuser(self):
        return self.is_admin

    