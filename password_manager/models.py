from django.db import models

# Create your models here.
# password_manager/models.py
from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
