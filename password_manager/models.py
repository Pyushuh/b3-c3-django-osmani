# password_manager/models.py
from django.db import models
from django.urls import reverse


class Site(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('edit_site', args=[str(self.id)])
