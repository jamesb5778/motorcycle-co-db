from django.db import models

# Create your models here.

# Model for Motorcycle company
class Motorcycle_Company(models.Model):
    name = models.CharField(max_length = 100)
    image = models.CharField(max_length = 500)
    founded = models.CharField(max_length = 25)
    description = models.TextField(max_length = 9999)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]