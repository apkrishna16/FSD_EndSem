from django.db import models
from shop.models import Plant

class PlantLibrary(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    information = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.plant.common_name
