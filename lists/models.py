from django.db import models


# Create your models here.
class Item(models.Model):
    objects = models.Manager()
    text = models.TextField(default='')
