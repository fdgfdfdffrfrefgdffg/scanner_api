from django.db import models

# Create your models here.
class Oquvchi(models.Model):
    ism_familya = models.CharField(max_length=100)
    sinf = models.CharField(max_length=4)
    maktab = models.SmallIntegerField()
    face_url = models.CharField(max_length=300)
