from django.db import models

# Create your models here.
class Oquvchi(models.Model):
    ism_familya = models.CharField(max_length=100)
    sinf = models.CharField(max_length=4)
    maktab = models.SmallIntegerField()
    phone = models.CharField(max_length=15)
    manzil = models.CharField(max_length=100)

    face_data = models.TextField()
    face_img = models.TextField()

