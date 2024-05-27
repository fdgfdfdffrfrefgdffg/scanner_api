from django.db import models

# Create your models here.
class Admin(models.Model):
    login = models.CharField(max_length=30)
    parol = models.CharField(max_length=30)
    ism_familya = models.CharField(max_length=100)
    maktab = models.SmallIntegerField()