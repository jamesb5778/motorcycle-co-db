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
        
#Model for the Motorcycle models
class Motorcycle_Model(models.Model):
    name = models.CharField(max_length = 100)
    image = models.CharField(max_length = 500)
    year_created = models.CharField(max_length = 4)
    Specs = models.TextField(max_length = 500)
    company = models.ForeignKey(Motorcycle_Company, on_delete=models.CASCADE, related_name="mc_models", null=True)
    
    def __str__(self):
        return self.name
    