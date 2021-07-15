from django.db import models
from custom_users.models import Uzer
# Create your models here.


class Image(models.Model):
    caption = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Uzer, on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        Uzer, related_name='post_likes', symmetrical=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.caption

    def count_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(
        Image, on_delete=models.CASCADE, related_name="comments")
    sender = models.ForeignKey(Uzer, on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.body
