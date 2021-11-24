from django.db import models
from random import choice
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=14,null=True,blank=True)
    verified_phone = models.BooleanField(default=False)
