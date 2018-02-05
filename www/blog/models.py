from django.db import models

# Create your models here.
class Person(models.Model):
    account = models.CharField(max_length=30)
    passwd = models.CharField(max_length=30)