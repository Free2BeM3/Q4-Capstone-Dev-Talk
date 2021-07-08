from django.db import models
from custom_users.models import Uzer
# Create your models here.

class Image(models.Model):
    caption = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Uzer, on_delete=models.CASCADE)

    class Meta:
        ordering=['-created_at']

    def __str__(self):
        return self.caption