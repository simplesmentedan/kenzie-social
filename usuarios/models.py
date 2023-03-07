from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

# Create your models here.
