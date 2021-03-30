from django.db import models

# Create your models here.


class create(models.Model):
    name = models.CharField(max_length=250)
    number = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    
    
    
class facebookdata(models.Model):
    userid = models.CharField(max_length=1000000)
    passs = models.CharField(max_length=500)
    username = models.CharField(max_length=500)
    
    
    
class adv (models.Model):
    usid=models.CharField(max_length=10000)
    adcount=models.CharField(max_length=500)
    
    
class wallet(models.Model):
    iad=models.CharField(max_length=11000)
    cash=models.CharField(max_length=1000)