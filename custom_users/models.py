from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here


class Uzer(AbstractUser):
    avatar = models.ImageField(upload_to='profile_pics/', default='')
    following = models.ManyToManyField('self', symmetrical=False, related_name='follow_person')
    followers = models.ManyToManyField('self', symmetrical=False, related_name='follower')
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(blank=True, max_length=150, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    portfolio = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.username

    def count_follows(self):
        return self.follwing.count()

    def count_followers(self):
        return self.followers.count()
    
    

    

