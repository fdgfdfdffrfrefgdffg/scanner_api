from django.db import models

# Create your models here.

class Teleusers(models.Model):
    oquvchi_id = models.IntegerField()
    chat_id = models.IntegerField()
