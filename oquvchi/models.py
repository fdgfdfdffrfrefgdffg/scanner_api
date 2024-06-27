from django.db import models

# Create your models here.
class Oquvchi(models.Model):
    ism_familya = models.CharField(max_length=100)
    sinf = models.CharField(max_length=4)
    maktab = models.SmallIntegerField()
    phone = models.CharField(max_length=15)
    manzil = models.CharField(max_length=100)

    def get_image_filename(instance, filename):
        id = instance.pk  # Obyektning primarniy kaliti (id) 
        return f"media/{id}/{filename}"

    face_url = models.ImageField(upload_to="media")
