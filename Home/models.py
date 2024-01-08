from email.policy import default
from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=20,default='')
    email = models.CharField(max_length=50, default='')
    message = models.CharField(max_length=500 ,default='')
