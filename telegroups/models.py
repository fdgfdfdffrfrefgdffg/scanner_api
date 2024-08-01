from django.db import models

# Create your models here.

class Telegroup(models.Model):
    oquvchi_id = models.IntegerField()
    sinf = models.CharField(max_length=5)
    group_id = models.IntegerField()
    topic_id = models.IntegerField()

