from django.db import models


# Create your models here.
class Note(models.Model):
    note = models.TextField(null=False)
