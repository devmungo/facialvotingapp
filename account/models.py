from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    id_number = models.CharField(max_length=13)
    vote_status = models.BooleanField(default=0)