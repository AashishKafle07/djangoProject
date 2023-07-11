from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,*args, **kwargs):
        if not email:
            raise ValueError("Email should not be empty")
        email=self.normalize_email(email)
        user=self.model(email=email,*args, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, *args, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
    
        return self.create_user(email, password, **kwargs)

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=150,unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
