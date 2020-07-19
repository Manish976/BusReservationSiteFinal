from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
   user = models.OneToOneField(User,on_delete=models.CASCADE)
   phone = models.CharField(max_length=256, blank=True, null=True)
