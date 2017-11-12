from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    body = models.CharField(max_length=140)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Tweet by {}".format(self.user.username)
