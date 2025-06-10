from django.db import models

class ToyotaModel(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} {self.year}"
# Create your models here.
