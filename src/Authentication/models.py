from django.db import models

# Create your models here.
class Url(models.Model):
    url_id = models.AutoField(primary_key=True)
    link = models.CharField(max_length=100000000)
    short_link = models.CharField(max_length=10000)