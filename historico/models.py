from django.db import models

# Create your models here.


class Historico(models.Model):
    num = models.IntegerField()
    primo = models.BooleanField(default=True)