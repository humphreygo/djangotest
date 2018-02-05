from django.db import models

# Create your models here.
class People(models.Model):
    account = models.CharField(max_length = 30,label = '账户')
    passwd = models.CharField(max_length = 30, label = '密码')

