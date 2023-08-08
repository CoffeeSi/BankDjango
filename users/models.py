from django.db import models
from django.contrib.auth.models import AbstractUser

from cash.models import Money

# Create your models here.

class User(AbstractUser):
    cardg = models.ForeignKey(to=Money, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username
