from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here


class Uzer(AbstractUser):
    following = models.ManyToManyField(
        'self', symmetrical=False, related_name='follow_person')
    bio = models.TextField()
