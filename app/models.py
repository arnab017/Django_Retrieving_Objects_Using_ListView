from django.db import models

# Create your models here.

class Trainer(models.Model):
    tid = models.IntegerField(primary_key=True)
    tname = models.CharField(max_length=20)
    tsubject = models.CharField(max_length=15)

    def __str__(self):
        return self.tname