from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    manager = models.CharField(max_length=100,default="Sam Adams")
    department = models.CharField(max_length=80,default="Finance")