from django.db import models
from django.utils import timezone

class Chiqish(models.Model):
    oquvchi_id = models.IntegerField()
    sana = models.DateField()
    vaqt = models.TimeField()
