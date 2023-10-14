from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Userprofile(models.Model):
    user=models.OneToOneField(User,related_name='userprofil',on_delete=models.CASCADE)
