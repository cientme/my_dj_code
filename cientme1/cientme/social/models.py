from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.username)

class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
