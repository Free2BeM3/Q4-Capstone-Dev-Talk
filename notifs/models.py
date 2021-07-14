from django.db import models
from django.utils import timezone
from custom_users.models import Uzer
from uploads.models import Comment

# Create your models here.


class Notifs(models.Model):
    notification = models.IntegerField(null=True, blank=True)
    reciever = models.ForeignKey(
        Uzer, related_name='notif_to', on_delete=models.CASCADE, null=True)
    sender = models.ForeignKey(
        Uzer, related_name='notif_from', on_delete=models.CASCADE, null=True)
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='comment', blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    user_has_seen = models.BooleanField(default=False)
